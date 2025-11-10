"use client";
import { faUserPlus } from "@fortawesome/free-solid-svg-icons";
import { useState } from "react";
import BotaoGenerico from "../components/botao";
import Menu from "../components/menu";
import styles from "../styles/pagina.module.css";
import TabelaTimes from "../components/listar_time";
import CriarTime from "../components/criarTime";

export default function TimesPage() {
  const [showPopup, setShowPopup] = useState(false);
  return (
    <div>
      <Menu />

      <div className={styles.container}>
        <BotaoGenerico
          texto="Adicionar Time"
          icone={faUserPlus}
          onClick={() => setShowPopup(true)}
        />

        {showPopup && (
          <div className={styles.popupOverlay}>
            <div className={styles.popupContent}>
              <CriarTime onClose={() => setShowPopup(false)} />
            </div>
          </div>
        )}
      </div>

      <TabelaTimes />
    </div>
  );
}
