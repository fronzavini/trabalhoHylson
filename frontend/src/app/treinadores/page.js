"use client";
import { faUserPlus } from "@fortawesome/free-solid-svg-icons";
import { useState } from "react";
import BotaoGenerico from "../components/botao";
import Menu from "../components/menu";
import styles from "../styles/pagina.module.css";
import TabelaTreinadores from "../components/listar_treinador";
import CriarTreinador from "../components/criarTreinador";

export default function TreinadoresPage() {
  const [showPopup, setShowPopup] = useState(false);
  return (
    <div>
      <Menu />

      <div className={styles.container}>
        <BotaoGenerico
          texto="Adicionar Treinador"
          icone={faUserPlus}
          onClick={() => setShowPopup(true)}
        />

        {showPopup && (
          <div className={styles.popupOverlay}>
            <div className={styles.popupContent}>
              <CriarTreinador onClose={() => setShowPopup(false)} />
            </div>
          </div>
        )}
      </div>

      <TabelaTreinadores />
    </div>
  );
}
