"use client";

import CriarAtleta from "../components/criarAtleta";
import Menu from "../components/menu";

export default function AtletasPage() {
  return (
    <div>
      <Menu />
      <h1>Cadastro de Atletas</h1>
      <CriarAtleta />
    </div>
  );
}
