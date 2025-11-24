import Link from "next/link";
import styles from "../styles/menu.module.css";

export default function Menu() {
  return (
    <nav className={styles.nav}>
      <ul className={styles.menu}>
        <li className={styles.item}>
          <Link href="/">Home</Link>
        </li>
        <li className={styles.item}>
          <Link href="/atletas">Atletas</Link>
        </li>
        <li className={styles.item}>
          <Link href="/treinadores">Treinadores</Link>
        </li>
        <li className={styles.item}>
          <Link href="/times">Times</Link>
        </li>
        <li className={styles.item}>
          <Link href="/treino">Treino</Link>
        </li>
      </ul>
    </nav>
  );
}
