package com.gssoa.model;

import jakarta.persistence.*;

@Entity
public class Bairro {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String nome;
    private Integer tempoEstimado;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public Integer getTempoEstimado() {
        return tempoEstimado;
    }

    public void setTempoEstimado(Integer tempoEstimado) {
        this.tempoEstimado = tempoEstimado;
    }
}