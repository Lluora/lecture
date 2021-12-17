package com.sparta.weeklytestspring.repository;

import com.sparta.weeklytestspring.domain.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
}
