"use client";
import { useState } from "react";
import axios from "axios";
import styles from "../styles/form.module.css";

export default function CriarTreinador({ onClose }) {
  const [formData, setFormData] = useState({
    nome: "",
    dt_nasc: "",
    email: "",
    cpf: "",
    cref: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post(
        "http://localhost:5000/treinadores",
        formData,
        {
          headers: { "Content-Type": "application/json" },
        }
      );

      if (res.data.result === "ok") {
        alert("Treinador criado com sucesso!");
        if (onClose) onClose();
      } else {
        alert("Erro: " + res.data.details);
      }
    } catch (err) {
      console.error("Erro ao salvar treinador:", err);
      alert("Erro ao salvar treinador");
    }
  };

  return (
    <div className={styles.formWrapper}>
      {onClose && (
        <button className={styles.closeBtn} onClick={onClose}>
          ✕
        </button>
      )}

      <form className={styles.form} onSubmit={handleSubmit}>
        <h2>Criar Treinador</h2>

        <label className={styles.label}>
          Nome:
          <input
            type="text"
            name="nome"
            value={formData.nome}
            onChange={handleChange}
            required
            className={styles.input}
          />
        </label>

        <label className={styles.label}>
          Data de Nascimento:
          <input
            type="date"
            name="dt_nasc"
            value={formData.dt_nasc}
            onChange={handleChange}
            required
            className={styles.input}
          />
        </label>

        <label className={styles.label}>
          Email:
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
            className={styles.input}
          />
        </label>

        <label className={styles.label}>
          CPF:
          <input
            type="text"
            name="cpf"
            value={formData.cpf}
            onChange={handleChange}
            required
            className={styles.input}
            placeholder="000.000.000-00"
            maxLength={14}
          />
        </label>

        <label className={styles.label}>
          CREF:
          <input
            type="text"
            name="cref"
            value={formData.cref}
            onChange={handleChange}
            className={styles.input}
            placeholder="Ex: CREF12345-G/RS"
          />
        </label>

        <button type="submit" className={styles.botao}>
          Criar Treinador
        </button>
      </form>
    </div>
  );
}
