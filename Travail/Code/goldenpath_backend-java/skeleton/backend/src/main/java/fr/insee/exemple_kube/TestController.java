package fr.insee.exemple_kube;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TestController {

    @Value("${environnement}")
    private String env;

    @GetMapping("hello")
    public String hello() {
        return "Hello World";
    }

    @GetMapping("environnement")
    public String env() {
        return env;
    }

}
