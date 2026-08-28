package fr.testlocal.applitestlocal.config;

import org.springdoc.core.customizers.OperationCustomizer;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import io.swagger.v3.oas.models.Components;
import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Info;
import io.swagger.v3.oas.models.security.*;

@Configuration
public class OpenApiConfig {

    private static final String SCHEMEKEYCLOAK = "oAuthScheme";

    @Value("${keycloak.auth-server-url}")
    private String keycloakUrl;

    @Value("${keycloak.realm}")
    private String realmName;

    @Value("${info.versionApplication}")
    private String version;

    @Bean
    public OpenAPI customOpenAPIKeycloak() {
        Scopes scopes = new Scopes();
        scopes.put("role-as-group", "obtenir les rôles");
        scopes.put("profile", "obtenir le nom, prénom, preferred username...");
        // configuration pour récupérer un jeton auprès de Keycloak
        final OpenAPI openapi = new OpenAPI()
                .info(
                        new Info()
                                .title("Swagger  API")
                                .version(version));
        String urlAuthentificationRoot = String.format("%s/realms/%s/protocol/openid-connect/", keycloakUrl, realmName);
        String urlAuthentificationGetToken = urlAuthentificationRoot + "token";
        String urlAuthentificationGetAuth = urlAuthentificationRoot + "auth";
        OAuthFlow flow = new OAuthFlow()
                .scopes(scopes)
                .authorizationUrl(urlAuthentificationGetAuth)
                .tokenUrl(urlAuthentificationGetToken)
                .refreshUrl(urlAuthentificationGetToken);
        OAuthFlows standardFlows = new OAuthFlows().authorizationCode(flow);
        SecurityScheme securityScheme = new SecurityScheme()
                .type(SecurityScheme.Type.OAUTH2)
                .in(SecurityScheme.In.HEADER)
                .description("Authentification keycloak")
                .flows(standardFlows);
        Components components = new Components().addSecuritySchemes(SCHEMEKEYCLOAK, securityScheme);
        openapi.components(components);
        return openapi;
    }

    @Bean
    public OperationCustomizer ajouterKeycloak() {
        // configuration pour que Swagger utilise le jeton récupéré auprès de Keycloak
        return (operation, handlerMethod) -> operation
                .addSecurityItem(new SecurityRequirement().addList(SCHEMEKEYCLOAK));
    }
}
