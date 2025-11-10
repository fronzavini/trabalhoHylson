"use client";
import { useEffect, useState } from "react";
import { DataTable } from "primereact/datatable";
import { Column } from "primereact/column";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTrash } from "@fortawesome/free-solid-svg-icons";

import styles from "../styles/tabela.module.css";

export default function ListarTreino() {
  const [treinos, setTreinos] = useState([]);

  const carregarTreinos = async () => {
    try {
      const res = await fetch("http://localhost:5000/treinos");
      const data = await res.json();

      if (!data || data.result !== "ok" || !Array.isArray(data.details)) {
        console.error("Erro ao listar treinos:", data?.details || "Inválido");
        return;
      }

      // 🔧 Formatar datas e campos compostos
      const formatados = data.details.map((t) => ({
        id: t.id,
        data: formatDate(t.data),
        horario: t.horario,
        time: t.time_nome || t.time,
        local: t.local,
        treinador: t.treinador_nome || t.treinador,
      }));

      setTreinos(formatados);
    } catch (err) {
      console.error("Erro ao carregar treinos:", err);
    }
  };

  const formatDate = (dateStr) => {
    if (!dateStr) return "";
    const d = new Date(dateStr);
    const day = String(d.getUTCDate()).padStart(2, "0");
    const month = String(d.getUTCMonth() + 1).padStart(2, "0");
    const year = d.getUTCFullYear();
    return `${day}/${month}/${year}`;
  };

  useEffect(() => {
    carregarTreinos();
  }, []);

  const actionTemplate = (rowData) => (
    <div className={styles.acoes}>
      <button
        className={styles.acaoBotao}
        onClick={async () => {
          if (
            !confirm(
              `Deseja realmente deletar o treino do dia ${rowData.data}?`
            )
          )
            return;
          try {
            const res = await fetch(
              `http://localhost:5000/treinos/${rowData.id}`,
              {
                method: "DELETE",
              }
            );
            if (!res.ok) throw new Error("Erro ao deletar treino");
            setTreinos((prev) => prev.filter((t) => t.id !== rowData.id));
          } catch (err) {
            console.error(err);
            alert("Erro ao deletar treino");
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
        value={treinos}
        paginator
        rows={6}
        showGridlines
        scrollable
        scrollHeight="500px"
        stripedRows
        emptyMessage="Nenhum treino cadastrado."
        responsiveLayout="scroll"
      >
        <Column field="id" header="ID" style={{ width: "80px" }} />
        <Column field="data" header="Data" />
        <Column field="horario" header="Horário" />
        <Column field="time" header="Time" />
        <Column field="local" header="Local" />
        <Column field="treinador" header="Treinador" />
        <Column
          body={actionTemplate}
          header="Ações"
          style={{ textAlign: "center", width: "120px" }}
        />
      </DataTable>
    </div>
  );
}
