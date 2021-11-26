package com.sparta.weeklytestspring.controller;
import com.sparta.weeklytestspring.domain.Article;
import com.sparta.weeklytestspring.dto.ArticleCommentRequestDto;
import com.sparta.weeklytestspring.dto.ArticleRequestDto;
import com.sparta.weeklytestspring.service.ArticleService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RequiredArgsConstructor
@RestController
public class ArticleController {
    private final ArticleService articleService;

    @PostMapping("/article")// 글 포스팅
    public Article setArticle(@RequestBody ArticleRequestDto articleRequestDto){
        return articleService.setArticle(articleRequestDto);
    }

    @GetMapping("/articles") // 본문 띄우기
    public List<Article> getArticles(){
        return articleService.getArticles();
    }

    @GetMapping("/article/{id}") // 제목 클릭
    public Article getArticle(@PathVariable Long id){
        return articleService.getArticle(id);
    }

    @PostMapping("/article/comment") // 댓글 달기
    public void  setArticleComment(@RequestBody ArticleCommentRequestDto articleCommentRequestDto){
        articleService.setArticleComment(articleCommentRequestDto);
    }

    @GetMapping("/articles/searchTag={tag}")
    public List<Article> getTags(){
        return articleService.getArticles();
    }

}
