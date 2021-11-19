package com.example.test2.model;

import com.example.test2.dto.TextDto;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Getter
@Setter
@NoArgsConstructor
@Entity
public class Text {
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Id
    private Long id;

    private String text;

    public Text(TextDto shortTextDto) {
        this.text = shortTextDto.getText();
    }
}
