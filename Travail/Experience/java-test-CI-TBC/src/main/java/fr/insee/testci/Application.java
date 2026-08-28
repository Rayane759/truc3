package fr.insee.testci;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import fr.insee.testci.config.PropertiesLogger;

@SpringBootApplication
public class Application {

    public static void main(String[] args) {
        SpringApplication sa = new SpringApplication(Application.class);
        sa.addListeners(new PropertiesLogger());
        sa.run(args);

    }
}
