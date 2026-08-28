package fr.insee.sndil.starter.controller;

import org.springframework.boot.info.BuildProperties;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@RequestMapping("/helloworld")
@Controller
@ResponseBody
public class HelloworldController {
    

    @GetMapping("/")
    public String sayHello(){
            return "HelloWorld";
    }
}
