"use client";
import { useState, useEffect } from "react";
import { DataTable } from "primereact/datatable";
import { Column } from "primereact/column";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTrash } from "@fortawesome/free-solid-svg-icons";
import styles from "../styles/tabela.module.css";

export default function TabelaAtletas() {
  const [atletas, setAtletas] = useState([]);
  const [times, setTimes] = useState([]);

  const formatDate = (dateStr) => {
    if (!dateStr) return "";
    const d = new Date(dateStr);
    const day = String(d.getUTCDate()).padStart(2, "0");
    const month = String(d.getUTCMonth() + 1).padStart(2, "0");
    const year = d.getUTCFullYear();
    return `${day}/${month}/${year}`;
  };

  // 🔹 Carrega atletas, fotos e times
  const carregarAtletas = async () => {
    try {
      const [resAtletas, resFotos, resTimes] = await Promise.all([
        fetch("http://www.pythonanywhere.com/atletas"),
        fetch("http://www.pythonanywhere.com/fotos"),
        fetch("http://www.pythonanywhere.com/times"),
      ]);

      const dataAtletas = await resAtletas.json();
      const dataFotos = await resFotos.json();
      const dataTimes = await resTimes.json();

      if (
        !dataAtletas ||
        dataAtletas.result !== "ok" ||
        !Array.isArray(dataAtletas.details)
      ) {
        console.error(
          "Erro ao listar atletas:",
          dataAtletas?.details || "Resposta inválida"
        );
        return;
      }

      // Mapa de fotos
      const fotosMap = {};
      if (dataFotos.result === "ok" && Array.isArray(dataFotos.details)) {
        dataFotos.details.forEach((f) => (fotosMap[f.id] = f));
      }

      // Mapa de times
      const timesMap = {};
      if (dataTimes.result === "ok" && Array.isArray(dataTimes.details)) {
        dataTimes.details.forEach((t) => (timesMap[t.id] = t));
        setTimes(dataTimes.details);
      }

      // Formata atletas
      const formatados = dataAtletas.details.map((a) => {
        const atletaTimes = (a.times_ids || a.times || []).map((tid) => {
          // dependendo do backend, pode vir como id ou objeto
          if (typeof tid === "object") return tid;
          return timesMap[tid] || { id: tid, nome: "Desconhecido" };
        });

        return {
          id: a.id,
          nome: a.nome,
          dt_nasc: formatDate(a.dt_nasc),
          email: a.email,
          cpf: a.cpf,
          ft_perfil: a.ft_perfil ? fotosMap[a.ft_perfil] : null,
          times: atletaTimes,
        };
      });

      setAtletas(formatados);
    } catch (err) {
      console.error("Erro ao carregar atletas:", err);
    }
  };

  useEffect(() => {
    carregarAtletas();
  }, []);

  const fotoTemplate = (rowData) =>
    rowData.ft_perfil?.url ? (
      <img
        src={rowData.ft_perfil.url}
        alt={rowData.nome}
        className={styles.fotoPerfil}
      />
    ) : (
      <span className={styles.semFoto}>Sem foto</span>
    );

  const timesTemplate = (rowData) =>
    rowData.times && rowData.times.length > 0 ? (
      <div className={styles.timesContainer}>
        {rowData.times.map((time) => (
          <span key={time.id} className={styles.timeBadge}>
            {time.nome || time.esporte}
          </span>
        ))}
      </div>
    ) : (
      <span className={styles.semTimes}>Sem times</span>
    );

  const actionTemplate = (rowData) => (
    <div className={styles.acoes}>
      <button
        className={styles.acaoBotao}
        onClick={async () => {
          if (!confirm(`Deseja realmente deletar o atleta "${rowData.nome}"?`))
            return;
          try {
            const res = await fetch( 'http://www.pythonanywhere.com/atletas/${rowData.id}`,
              { method: "DELETE" }
            );
            if (!res.ok) throw new Error("Erro ao deletar atleta");
            setAtletas((prev) => prev.filter((a) => a.id !== rowData.id));
          } catch (err) {
            console.error(err);
            alert("Erro ao deletar atleta");
          }
        }}
        title="Excluir"
      >
        <FontAwesomeIcon icon={faTrash} />
      </button>
    </div>
  );

  return (
    <div className={styles["custom-table-container"]}>
      <DataTable
        value={atletas}
        paginator
        rows={5}
        showGridlines
        scrollable
        scrollHeight="500px"
      >
        <Column field="id" header="ID" />
        <Column field="nome" header="Nome" />
        <Column field="dt_nasc" header="Data Nascimento" />
        <Column field="email" header="Email" />
        <Column field="cpf" header="CPF" />
        <Column header="Foto" body={fotoTemplate} />
        <Column header="Times" body={timesTemplate} />
        <Column
          body={actionTemplate}
          header="Ações"
          style={{ width: "150px" }}
        />
      </DataTable>
    </div>
  );
}
