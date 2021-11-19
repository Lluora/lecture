package com.example.test2.Service;

import com.example.test2.Repository.TextRepository;
import com.example.test2.dto.TextDto;
import com.example.test2.model.Text;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;
import java.util.List;

@Service
public class TextService {

    private final TextRepository TextRepository;

    @Autowired
    public TextService(TextRepository TextRepository) {
        this.TextRepository = TextRepository;
    }

    public List<Text> getTexts() {
        return TextRepository.findAll();
    }

    @Transactional
    public Text createText(TextDto TextDto){
        Text Text = new Text(TextDto);

        TextRepository.save(Text);

        return Text;
    }
}
