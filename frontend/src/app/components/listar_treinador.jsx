"use client";
import { useState, useEffect } from "react";
import { DataTable } from "primereact/datatable";
import { Column } from "primereact/column";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTrash } from "@fortawesome/free-solid-svg-icons";
import styles from "../styles/tabela.module.css";


export default function TabelaTreinadores() {
  const [treinadores, setTreinadores] = useState([]);

  const formatDate = (dateStr) => {
    if (!dateStr) return "";
    const d = new Date(dateStr);
    const day = String(d.getUTCDate()).padStart(2, "0");
    const month = String(d.getUTCMonth() + 1).padStart(2, "0");
    const year = d.getUTCFullYear();
    return `${day}/${month}/${year}`;
  };

  const carregarTreinadores = async () => {
    try {
      const res = await fetch("http://localhost:5000/treinadores");
      const data = await res.json();

      if (!data || data.result !== "ok" || !Array.isArray(data.details)) {
        console.error(
          "Erro ao listar treinadores:",
          data?.details || "Resposta inválida"
        );
        return;
      }

      const formatados = data.details.map((t) => ({
        ...t,
        dt_nasc: formatDate(t.dt_nasc),
      }));

      setTreinadores(formatados);
    } catch (err) {
      console.error("Erro ao carregar treinadores:", err);
    }
  };

  useEffect(() => {
    carregarTreinadores();
  }, []);

  const actionTemplate = (rowData) => (
    <div className={styles.acoes}>
      <button
        className={styles.acaoBotao}
        onClick={async () => {
          if (
            !confirm(`Deseja realmente deletar o treinador "${rowData.nome}"?`)
          )
            return;
          try {
            const res = await fetch(
              `http://localhost:5000/treinadores/${rowData.id}`,
              {
                method: "DELETE",
              }
            );
            if (!res.ok) throw new Error("Erro ao deletar treinador");
            setTreinadores((prev) => prev.filter((t) => t.id !== rowData.id));
          } catch (err) {
            console.error(err);
            alert("Erro ao deletar treinador");
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
        value={treinadores}
        paginator
        rows={5}
        showGridlines
        scrollable
        scrollHeight="400px"
      >
        <Column field="id" header="ID" />
        <Column field="nome" header="Nome" />
        <Column field="dt_nasc" header="Data Nascimento" />
        <Column field="email" header="Email" />
        <Column field="cpf" header="CPF" />
        <Column field="cref" header="CREF" />
        <Column
          body={actionTemplate}
          header="Ações"
          style={{ width: "100px" }}
        />
      </DataTable>

    </div>
  );
}
