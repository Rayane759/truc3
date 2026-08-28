package fr.testlocal.applitestlocal.controller ;

import fr.testlocal.applitestlocal.service.ExampleService ;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.context.annotation.Import;
import org.springframework.test.web.servlet.MockMvc;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@WebMvcTest(TaskController.class)
@Import(ExampleService.class)
class TaskControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Test
    void shouldCreateAndFetchTask() throws Exception {

        // Create
        mockMvc.perform(post("/api/tasks")
                .contentType("application/json")
                .content("{\"title\":\"My task\"}"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.title").value("My task"));

        // Fetch all
        mockMvc.perform(get("/api/tasks"))
                .andExpect(status().isOk());
    }
}
