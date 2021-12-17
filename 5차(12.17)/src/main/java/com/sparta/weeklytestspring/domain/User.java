package com.sparta.weeklytestspring.domain;


import com.sparta.weeklytestspring.dto.UserRequestDto;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.springframework.web.servlet.handler.UserRoleAuthorizationInterceptor;

import javax.persistence.*;

@AllArgsConstructor
@NoArgsConstructor
@Setter
@Getter
@Entity
public class User {
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Id
    @Column(name = "UserId")
    private Long idx;

    @Column(nullable = false)
    private String id;

    @Column(nullable = false)
    private String pwd;


    public User(UserRequestDto userRequestDto) {
        this.id = userRequestDto.getId();
        this.pwd = userRequestDto.getPwd();
    }
}
