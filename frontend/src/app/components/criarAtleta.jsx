import { useState, useEffect } from "react";
import axios from "axios";
import styles from "../styles/form.module.css";

export default function CriarAtleta({ onClose }) {
  const [times, setTimes] = useState([]);
  const [formData, setFormData] = useState({
    nome: "",
    dt_nasc: "",
    email: "",
    cpf: "",
    foto_url: "",
    times_ids: [],
  });

  useEffect(() => {
    axios
      .get("http://localhost:5000/times")
      .then((res) => {
        if (res.data.result === "ok" && Array.isArray(res.data.details)) {
          setTimes(res.data.details);
        } else {
          setTimes([]);
        }
      })
      .catch(() => setTimes([]));
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleTimesChange = (e) => {
    const selectedOptions = Array.from(e.target.selectedOptions);
    const ids = selectedOptions.map((opt) => Number(opt.value));
    setFormData((prev) => ({ ...prev, times_ids: ids }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("http://localhost:5000/atletas", formData, {
        headers: { "Content-Type": "application/json" },
      });

      if (res.data.result === "ok") {
        alert("Atleta criado com sucesso!");
        setFormData({
          nome: "",
          dt_nasc: "",
          email: "",
          cpf: "",
          foto_url: "",
          times_ids: [],
        });
        if (onClose) onClose(); // Fecha o form após criar
      } else {
        alert("Erro ao criar atleta: " + res.data.details);
      }
    } catch (err) {
      console.error("Erro ao criar atleta:", err);
      alert("Erro ao criar atleta");
    }
  };

  return (
    <div className={styles.formWrapper}>
      {/* Botão de fechar */}
      {onClose && (
        <button className={styles.closeBtn} onClick={onClose}>
          ✕
        </button>
      )}
      <form className={styles.form} onSubmit={handleSubmit}>
        <label className={styles.label}>
          Nome do atleta:
          <input
            type="text"
            name="nome"
            value={formData.nome}
            onChange={handleChange}
            className={styles.input}
            required
          />
        </label>

        <label className={styles.label}>
          Data de nascimento:
          <input
            type="date"
            name="dt_nasc"
            value={formData.dt_nasc}
            onChange={handleChange}
            className={styles.input}
            required
          />
        </label>

        <label className={styles.label}>
          Email:
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            className={styles.input}
            required
          />
        </label>

        <label className={styles.label}>
          CPF:
          <input
            type="text"
            name="cpf"
            value={formData.cpf}
            onChange={handleChange}
            className={styles.input}
            required
          />
        </label>

        <label className={styles.label}>
          Foto (URL):
          <input
            type="text"
            name="foto_url"
            value={formData.foto_url}
            onChange={handleChange}
            className={styles.input}
          />
        </label>

        <label className={styles.label}>
          Times (segure Ctrl para selecionar vários):
          <select
            multiple
            name="times_ids"
            value={formData.times_ids}
            onChange={handleTimesChange}
            className={styles.select}
          >
            {(Array.isArray(times) ? times : []).map((time) => (
              <option key={time.id} value={time.id}>
                {time.esporte}
              </option>
            ))}
          </select>
        </label>

        <button type="submit" className={styles.botao}>
          Criar Atleta
        </button>
      </form>
    </div>
  );
}
