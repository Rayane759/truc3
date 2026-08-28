package fr.insee.testci.config;


import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.security.config.Customizer;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configurers.AbstractHttpConfigurer;
import org.springframework.security.config.annotation.web.configurers.AuthorizeHttpRequestsConfigurer;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.authentication.session.NullAuthenticatedSessionStrategy;
import org.springframework.web.cors.CorsConfiguration;
import org.springframework.web.cors.CorsConfigurationSource;
import org.springframework.web.cors.UrlBasedCorsConfigurationSource;

@Configuration
public class SecurityConfig {
    
    private static final Logger log = LoggerFactory.getLogger(SecurityConfig.class);
    public static final String ADMIN = "CHANGE_ME";

    @Value("${app.security.allowed-origins:*}")
    private String allowedOrigins;

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) {
        // fonctionnement du filtre CORS avec Spring Security
        // chargement de la configuration CORS définie dans un Bean
        // CORS doit être traité en premier, sinon Spring Secu rejettera la demande
        http.cors(Customizer.withDefaults());
        // désactivation CSRF car API (ne pas faire dans le cas d'une appli avec JSP)
        http.csrf(AbstractHttpConfigurer::disable);
        // désactivation des cookies de session
        // (ne pas faire dans le cas d'une appli avec JSP)
        http.sessionManagement(
                session -> session.sessionAuthenticationStrategy(
                        new NullAuthenticatedSessionStrategy())
                        .sessionCreationPolicy(SessionCreationPolicy.STATELESS));
        // autoriser l'authentification par jeton JWT
        http.oauth2ResourceServer(oauth2 -> oauth2.jwt(jwtConfigurer -> Customizer.withDefaults()));
        http.authorizeHttpRequests(this::authorizedUrls);

        return http.build();
    }

    private void authorizedUrls(
            AuthorizeHttpRequestsConfigurer<HttpSecurity>.AuthorizationManagerRequestMatcherRegistry authorize) {
        String[] urlsSwagger = { "/", "/swagger-ui.html", "/swagger-ui/**", "/v3/api-docs/**" };
        String[] urlsDivers = { "/healthcheck/**" };
        // gestion de nos endpoints
        for (String url : urlsSwagger) {
            authorize.requestMatchers(HttpMethod.GET, url).permitAll();
        }
        for (String url : urlsDivers) {
            authorize.requestMatchers(HttpMethod.GET, url).permitAll();
        }
        
        // jeton nécessaire pour toutes les autres requêtes
        authorize.anyRequest().hasAnyRole(ADMIN);
    }

    @Bean
    public CorsConfigurationSource corsConfigurationSource() {
        log.info(
                "URLs autorisées pour faire des requêtes HTTP depuis le navigateur : {}",
                List.of(allowedOrigins));
        CorsConfiguration configuration = new CorsConfiguration();
        configuration.setAllowedOriginPatterns(List.of(allowedOrigins));
        configuration.setAllowedMethods(List.of("*"));
        configuration.setAllowedHeaders(List.of("*"));
        configuration.setMaxAge(3600L);
        configuration.setExposedHeaders(List.of(HttpHeaders.CONTENT_DISPOSITION));
        UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
        source.registerCorsConfiguration("/**", configuration);
        return source;
    }
}
