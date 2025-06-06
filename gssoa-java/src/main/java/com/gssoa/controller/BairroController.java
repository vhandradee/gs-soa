package com.gssoa.controller;

import com.gssoa.model.Bairro;
import com.gssoa.repository.BairroRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/bairros")
public class BairroController {

    @Autowired
    private BairroRepository bairroRepository;

    @GetMapping
    public List<Bairro> listarBairros() {
        return bairroRepository.findAll();
    }

    @PostMapping
    public Bairro adicionarBairro(@RequestBody Bairro bairro) {
        return bairroRepository.save(bairro);
    }
}