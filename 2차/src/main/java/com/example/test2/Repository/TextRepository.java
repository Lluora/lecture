package com.example.test2.Repository;


import com.example.test2.model.Text;
import org.springframework.data.jpa.repository.JpaRepository;

public interface TextRepository extends JpaRepository<Text, Long> {

}
