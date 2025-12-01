import { useState } from "react";
import axios from "axios";
import styles from "../styles/form.module.css";

export default function CriarTime({ onClose }) {
  const [formData, setFormData] = useState({
    esporte: "",
  });

  const handleChange = (e) => {
    setFormData({ ...formData, esporte: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post("http://www.pythonanywhere.com/times", formData, {
        headers: { "Content-Type": "application/json" },
      });

      if (res.data.result === "ok") {
        alert("Time criado com sucesso!");
        if (onClose) onClose();
      } else {
        alert("Erro: " + res.data.details);
      }
    } catch (err) {
      console.error("Erro ao salvar time:", err);
      alert("Erro ao salvar time");
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
        <h2>Criar Time</h2>

        <label className={styles.label}>
          Nome:
          <input
            type="text"
            name="esporte"
            value={formData.esporte}
            onChange={handleChange}
            required
            className={styles.input}
          />
        </label>

        <button type="submit" className={styles.botao}>
          Criar Time
        </button>
      </form>
    </div>
  );
}
