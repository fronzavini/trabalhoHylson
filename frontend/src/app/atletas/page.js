"use client";
import { faUserPlus } from "@fortawesome/free-solid-svg-icons";
import { useState } from "react";
import BotaoGenerico from "../components/botao";
import CriarAtleta from "../components/criarAtleta";
import Menu from "../components/menu";
import styles from "../styles/pagina.module.css";
import ListarAtletas from "../components/listar_atleta";

export default function AtletasPage() {
  const [showPopup, setShowPopup] = useState(false);
  return (
    <div>
      <Menu />

      <div className={styles.container}>
        <BotaoGenerico
          texto="Adicionar Atleta"
          icone={faUserPlus}
          onClick={() => setShowPopup(true)}
        />

        {showPopup && (
          <div className={styles.popupOverlay}>
            <div className={styles.popupContent}>
              <CriarAtleta onClose={() => setShowPopup(false)} />
            </div>
          </div>
        )}

        <ListarAtletas />
      </div>
    </div>
  );
}
