package fr.testlocal.applitestlocal.controller;

import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import fr.insee.exemple_kube.Application;
import fr.insee.exemple_kube.service.ExampleService;

@RestController
@RequestMapping("/api/tasks")
public class TaskController {

    private final ExampleService exampleService;

    public TaskController(ExampleService exampleService) {
        this.exampleService = exampleService;
    }

    @GetMapping
    public List<Application> getAllTasks() {
        return exampleService.findAll();
    }

    @GetMapping("/{id}")
    public Application getTask(@PathVariable Long id) {
        return exampleService.findById(id);
    }

    @PostMapping
    public Application createTask(@RequestBody Application task) {
        return exampleService.create(task.getTitle());
    }
}