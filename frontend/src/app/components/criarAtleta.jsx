import { useState, useEffect } from "react";
import axios from "axios";
import styles from "../styles/form.module.css";

export default function CriarAtleta({ onClose, atletaEditando }) {
  const [times, setTimes] = useState([]);
  const [formData, setFormData] = useState({
    nome: "",
    dt_nasc: "",
    email: "",
    cpf: "",
    foto_url: "",
    times_ids: [],
  });

  // 🔧 Converte datas para formato YYYY-MM-DD
  function toInputDate(value) {
    if (!value) return "";

    const isoMatch =
      typeof value === "string" && value.match(/^(\d{4}-\d{2}-\d{2})/);
    if (isoMatch) return isoMatch[1];

    const brMatch =
      typeof value === "string" && value.match(/^(\d{2})\/(\d{2})\/(\d{4})$/);
    if (brMatch) return `${brMatch[3]}-${brMatch[2]}-${brMatch[1]}`;

    const parsed = new Date(value);
    if (!isNaN(parsed)) {
      const y = parsed.getFullYear();
      const m = String(parsed.getMonth() + 1).padStart(2, "0");
      const d = String(parsed.getDate()).padStart(2, "0");
      return `${y}-${m}-${d}`;
    }

    return "";
  }

  //  Carrega times disponíveis
  useEffect(() => {
    axios
      .get( "http://www.pythonanywhere.com/times")
      .then((res) => {
        if (res.data.result === "ok" && Array.isArray(res.data.details)) {
          setTimes(res.data.details);
        } else {
          setTimes([]);
        }
      })
      .catch(() => setTimes([]));
  }, []);

  // ✏️ Preenche dados do atleta se estiver editando
  useEffect(() => {
    if (atletaEditando) {
      setFormData({
        nome: atletaEditando.nome || "",
        dt_nasc: toInputDate(atletaEditando.dt_nasc),
        email: atletaEditando.email || "",
        cpf: atletaEditando.cpf || "",
        foto_url: atletaEditando.foto_url || "",
        // converte ids para string para o select
        times_ids: atletaEditando.times
          ? atletaEditando.times.map((t) => t.id.toString())
          : [],
      });
    }
  }, [atletaEditando]);

  // 🖋️ Atualiza valores do formulário
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  // 🎯 Atualiza times selecionados
  const handleTimesChange = (e) => {
    const ids = Array.from(e.target.selectedOptions).map((opt) => opt.value);
    setFormData((prev) => ({ ...prev, times_ids: ids }));
  };

  // 💾 Envia formulário (POST ou PUT)
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const url = atletaEditando
        ? `http://www.pythonanywhere.com/atletas/${atletaEditando.id}`
        : "http://www.pythonanywhere.com/atletas";

      const metodo = atletaEditando ? "put" : "post";

      // converte times_ids de volta para números antes de enviar
      const payload = {
        ...formData,
        times_ids: formData.times_ids.map(Number),
      };

      const res = await axios[metodo](url, payload, {
        headers: { "Content-Type": "application/json" },
      });

      if (res.data.result === "ok") {
        alert(
          atletaEditando
            ? "Atleta atualizado com sucesso!"
            : "Atleta criado com sucesso!"
        );
        if (onClose) onClose();
      } else {
        alert("Erro: " + res.data.details);
      }
    } catch (err) {
      console.error("Erro ao salvar atleta:", err);
      alert("Erro ao salvar atleta");
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
        <h2>{atletaEditando ? "Editar Atleta" : "Criar Atleta"}</h2>

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
          Times (Ctrl para selecionar vários):
          <select
            multiple
            name="times_ids"
            value={formData.times_ids}
            onChange={handleTimesChange}
            className={styles.select}
          >
            {times.map((t) => (
              <option key={t.id} value={t.id.toString()}>
                {t.esporte}
              </option>
            ))}
          </select>
        </label>

        <button type="submit" className={styles.botao}>
          {atletaEditando ? "Salvar Alterações" : "Criar Atleta"}
        </button>
      </form>
    </div>
  );
}
