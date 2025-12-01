"use client";
import { useState, useEffect } from "react";
import { DataTable } from "primereact/datatable";
import { Column } from "primereact/column";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTrash } from "@fortawesome/free-solid-svg-icons";

import styles from "../styles/tabela.module.css";

export default function TabelaTimes() {
  const [times, setTimes] = useState([]);

  const carregarTimes = async () => {
    try {
      const res = await fetch("http://www.pythonanywhere.com/times");
      const data = await res.json();

      if (!data || data.result !== "ok" || !Array.isArray(data.details)) {
        console.error(
          "Erro ao listar times:",
          data?.details || "Resposta inválida"
        );
        return;
      }

      setTimes(data.details);
    } catch (err) {
      console.error("Erro ao carregar times:", err);
    }
  };

  useEffect(() => {
    carregarTimes();
  }, []);

  const actionTemplate = (rowData) => (
    <div className={styles.acoes}>
      <button
        className={styles.acaoBotao}
        onClick={async () => {
          if (!confirm(`Deseja realmente deletar o time "${rowData.esporte}"?`))
            return;
          try {
            const res = await fetch( 'http://www.pythonanywhere.com/times/${rowData.id',
              {
                method: "DELETE",
              }
            );
            if (!res.ok) throw new Error("Erro ao deletar time");
            setTimes((prev) => prev.filter((t) => t.id !== rowData.id));
          } catch (err) {
            console.error(err);
            alert("Erro ao deletar time");
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
        value={times}
        paginator
        rows={5}
        showGridlines
        scrollable
        scrollHeight="400px"
      >
        <Column field="id" header="ID" />
        <Column field="esporte" header="Nome / Esporte" />
        <Column
          body={actionTemplate}
          header="Ações"
          style={{ width: "150px" }}
        />
      </DataTable>
    </div>
  );
}
