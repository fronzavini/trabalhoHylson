import { useState, useEffect } from "react";
import axios from "axios";
import styles from "../styles/form.module.css";

export default function CriarAtleta() {
  const [times, setTimes] = useState([]);
  const [formData, setFormData] = useState({
    nome: "",
    dt_nasc: "",
    email: "",
    cpf: "",
    foto_url: "",
    times_ids: [],
  });

  // Buscar lista de times
  useEffect(() => {
    axios
      .get("http://localhost:5000/times")
      .then((res) => {
        console.log("Resposta /times:", res.data);
        // Garante que times sempre será um array
        if (res.data.result === "ok" && Array.isArray(res.data.details)) {
          setTimes(res.data.details);
        } else {
          setTimes([]);
        }
      })
      .catch((err) => {
        console.error("Erro ao buscar times:", err);
        setTimes([]);
      });
  }, []);

  // Atualizar campos simples
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  // Atualizar seleção de times (vários)
  const handleTimesChange = (e) => {
    const selectedOptions = Array.from(e.target.selectedOptions);
    const ids = selectedOptions.map((opt) => Number(opt.value));
    setFormData((prev) => ({
      ...prev,
      times_ids: ids,
    }));
  };

  // Enviar formulário
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
      } else {
        alert("Erro ao criar atleta: " + res.data.details);
      }
    } catch (err) {
      console.error("Erro ao criar atleta:", err);
      alert("Erro ao criar atleta");
    }
  };

  return (
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
  );
}
