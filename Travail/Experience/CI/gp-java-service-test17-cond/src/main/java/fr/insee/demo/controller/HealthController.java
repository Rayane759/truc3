package fr.insee.demo.controller ;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Endpoint de base pour vérifier que l'application fonctionne.
 * À remplacer par vos endpoints.
 */
@RestController
public class HealthController {

    @GetMapping("/api/health")
    public String health() {
        return "OK";
    }
}