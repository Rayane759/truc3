package fr.testlocal.applitestlocal.service ;

import fr.testlocal.applitestlocal.Application ;
import fr.testlocal.applitestlocal.service.ExampleService ;

import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class ExampleServiceTest {

    private final ExampleService service = new ExampleService();

    @Test
    void shouldCreateTask() {
        Application task = service.create("Test task");

        assertThat(task.getId()).isNotNull();
        assertThat(task.getTitle()).isEqualTo("Test task");
    }
}
