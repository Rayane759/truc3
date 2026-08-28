package fr.testlocal.applitestlocal.service ;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicLong;

import org.springframework.stereotype.Service;

import fr.insee.exemple_kube.Application;

@Service
public class ExampleService {

    private final Map<Long, Application> tasks = new HashMap<>();
    private final AtomicLong idGenerator = new AtomicLong();

    public List<Application> findAll() {
        return new ArrayList<>(tasks.values());
    }

    public Application findById(Long id) {
        Application task = tasks.get(id);
        if (task == null) {
            throw new RuntimeException("Task not found");
        }
        return task;
    }

    public Application create(String title) {
        Long id = idGenerator.incrementAndGet();
        Application task = new Application(id, title);
        tasks.put(id, task);
        return task;
    }
}