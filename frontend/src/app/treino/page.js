"use client";
import { faUserPlus } from "@fortawesome/free-solid-svg-icons";
import { useState } from "react";
import BotaoGenerico from "../components/botao";
import Menu from "../components/menu";
import styles from "../styles/pagina.module.css";
import TabelaTreino from "../components/listar_treino";
import CriarTreino from "../components/criarTreino";

export default function AtletasPage() {
  const [showPopup, setShowPopup] = useState(false);
  return (
    <div>
      <Menu />

      <div className={styles.container}>
        <BotaoGenerico
          texto="Adicionar Treino"
          icone={faUserPlus}
          onClick={() => setShowPopup(true)}
        />

        {showPopup && (
          <div className={styles.popupOverlay}>
            <div className={styles.popupContent}>
              <CriarTreino onClose={() => setShowPopup(false)} />
            </div>
          </div>
        )}
      </div>

      <TabelaTreino />
    </div>
  );
}
