package fr.insee.tbc.testtobecontinuous.service ;

import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class ExampleServiceTest {

    private final ExampleService service = new ExampleService();

    @Test
    void shouldProcess() {
        String result = service.process();
        assertThat(result).isEqualTo("processed");
    }
}
