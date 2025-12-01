"use client";
import { useState, useEffect } from "react";
import axios from "axios";
import styles from "../styles/form.module.css";

export default function CriarTreino({ onClose }) {
  const [formData, setFormData] = useState({
    data: "",
    hora: "",
    local: "",
    time_id: "",
    treinador_id: "",
  });

  const [times, setTimes] = useState([]);
  const [treinadores, setTreinadores] = useState([]);

  // --- Carrega dados dos selects ---
  useEffect(() => {
    async function carregarDados() {
      try {
        const [resTimes, resTreinadores] = await Promise.all([
          axios.get( "http://www.pythonanywhere.com/times"),
          axios.get( "http://www.pythonanywhere.com/treinadores"),
        ]);

        if (resTimes.data.result === "ok") setTimes(resTimes.data.details);
        if (resTreinadores.data.result === "ok")
          setTreinadores(resTreinadores.data.details);
      } catch (error) {
        console.error("Erro ao carregar dados:", error);
      }
    }
    carregarDados();
  }, []);

  // --- Atualiza estado do formulário ---
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  // --- Envia o formulário ---
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const dataToSend = {
        data: formData.data,
        horario: formData.hora,
        local: formData.local,
        time: parseInt(formData.time_id),
        treinador: parseInt(formData.treinador_id),
      };

      const res = await axios.post( "http://www.pythonanywhere.com/treinos",
        dataToSend,
        {
          headers: { "Content-Type": "application/json" },
        }
      );

      if (res.data.result === "ok") {
        alert("Treino criado com sucesso!");
        if (onClose) onClose();
      } else {
        alert("Erro: " + res.data.details);
      }
    } catch (err) {
      console.error("Erro ao salvar treino:", err);
      alert("Erro ao salvar treino");
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
        <h2>Criar Treino</h2>

        <label className={styles.label}>
          Data:
          <input
            type="date"
            name="data"
            value={formData.data}
            onChange={handleChange}
            required
            className={styles.input}
          />
        </label>

        <label className={styles.label}>
          Hora:
          <input
            type="time"
            name="hora"
            value={formData.hora}
            onChange={handleChange}
            required
            className={styles.input}
          />
        </label>

        <label className={styles.label}>
          Local:
          <input
            type="text"
            name="local"
            value={formData.local}
            onChange={handleChange}
            required
            className={styles.input}
            placeholder="Ex: Ginásio Principal"
          />
        </label>

        <label className={styles.label}>
          Time:
          <select
            name="time_id"
            value={formData.time_id}
            onChange={handleChange}
            required
            className={styles.input}
          >
            <option value="">Selecione o time</option>
            {times.map((time) => (
              <option key={time.id} value={time.id}>
                {time.nome} ({time.esporte})
              </option>
            ))}
          </select>
        </label>

        <label className={styles.label}>
          Treinador:
          <select
            name="treinador_id"
            value={formData.treinador_id}
            onChange={handleChange}
            required
            className={styles.input}
          >
            <option value="">Selecione o treinador</option>
            {treinadores.map((t) => (
              <option key={t.id} value={t.id}>
                {t.nome}
              </option>
            ))}
          </select>
        </label>

        <button type="submit" className={styles.botao}>
          Criar Treino
        </button>
      </form>
    </div>
  );
}
