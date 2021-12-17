package com.sparta.weeklytestspring.service;

import com.sparta.weeklytestspring.domain.User;
import com.sparta.weeklytestspring.dto.UserRequestDto;
import com.sparta.weeklytestspring.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;
import java.io.IOException;


@RequiredArgsConstructor
@Service
public class UserService {
    private final UserRepository userRepository;

    @Transactional
    public User setUser(UserRequestDto userRequestDto)  {
        User user = new User(userRequestDto);
        return userRepository.save(user);
    }
}
