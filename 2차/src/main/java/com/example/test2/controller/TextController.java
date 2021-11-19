package com.example.test2.controller;


import com.example.test2.Service.TextService;
import com.example.test2.dto.TextDto;

import com.example.test2.model.Text;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class TextController {

    private final com.example.test2.Service.TextService TextService;

    @Autowired
    public TextController(TextService TextService){
        this.TextService = TextService;
    }

    @GetMapping("/api/get")
    public List<Text> getText(){
        return TextService.getTexts();
    }

    @PostMapping("/api/post")
    public Text createText(@RequestBody TextDto TextDto){
        Text shortText = TextService.createText(TextDto);
        System.out.println("테스트 성공");
        return shortText;
    }
}
