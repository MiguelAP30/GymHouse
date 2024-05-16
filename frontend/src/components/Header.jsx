import styled from "styled-components";
import img1 from "../assets/img/GymHouse.png";
import { HiMenuAlt2 } from "react-icons/hi";
import { MdClose } from "react-icons/md";
import { useState, useLayoutEffect } from "react";
import { useWindowScroll } from "react-use";
export function Header() {
  const [state, setState] = useState(false);
  const [stateHeader, setStateHeader] = useState(false);

  const { y } = useWindowScroll();

  useLayoutEffect(() => {
    if (y >= 50) {
      setStateHeader(true);
    } else {
      setStateHeader(false);
    }
  }, [y]);

  return (
    <Container>
      <header
        className={stateHeader ? "header bg-header" : "header"}
        id="header
        "
      >
        <nav class="nav container" >
          <a href="#" class="nav__logo">
          <img src={img1} alt="logo image" />
            GymHouse
          </a>

          <div
            className={state ? "nav__menu show-menu" : "nav__menu"}
            id="nav-menu"
          >
            <ul class="nav__list" onClick={() => setState(!state)}>
              <li class="nav__item">
                <a href="#home" class="nav__link active-link">
                  Inicio
                </a>
              </li>
              <li class="nav__item">
                <a href="#about" class="nav__link">
                  Acerca de
                </a>
              </li>
              <li class="nav__item">
                <a href="#items" class="nav__link">
                  Ejercicios
                </a>
              </li>
              <li class="nav__item">
                <a href="#party" class="nav__link">
                  Videos de apoyo
                </a>
              </li>

              <a class="button ">
                Iniciar
              </a>

              <a class="button ">
                Registrarse
              </a>
            </ul>

            <img src={img1} alt="nav image" class="nav__img" />
          </div>
        </nav>
      </header>
    </Container>
  );
}
const Container = styled.div`
  .header {
    position: fixed;
    width: 100%;
    background: transparent;
    top: 0;
    left: 0;
    z-index: var(--z-fixed);
    transition: background 0.3s, box-shadow 0.3s;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 10px;
  }


  .nav {
    position: relative;
    height: var(--header-height);
    display: flex;
    justify-content: space-between;
    align-items: center;

    &__logo,
    &__item,
    &__toggle,
    &__close {
      display: inline-flex;
      color: var(--white-color);
    }
    &__logo {
      align-items: center;
      column-gap: 0.5rem;
      font-weight: var(--font-medium);
      transition: color 0.3s;
      margin-right: 50px;

      & img {
        width: 1.25rem;
      }

      &:hover {
        color: var(--first-color);
      }
    }
    &__item {
      align-items: center;
      column-gap: 0.5rem;
      font-weight: var(--font-medium);
      transition: color 0.3s;
      margin-right: 50px;
    }
    &__toggle {
      font-size: 1.25rem;
      cursor: pointer;
    }
    &__menu {
      @media screen and (max-width: 767px) {
        position: fixed;
        top: -100%;
        left: 0;
        background-color: var(--body-color);
        width: 100%;
        box-shadow: 0 4px 8px hsla(22, 10%, 2%, 0.5);
        padding-block: 3.5rem 3rem;
        border-radius: 0 0 2rem 2rem;
        transition: top 0.4s;
      }
    }
    &__list {
      flex-direction: column;
      text-align: center;
      row-gap: 1.5rem;
    }
    &__link {
      color: var(--white-color);
      font-family: var(--second-font);
      transition: color 0.4s;

      &:hover {
        color: var(--first-color);
      }
    }
    &__close {
      position: absolute;
      top: 1rem;
      right: 1.5rem;
      font-size: 1.5rem;
      cursor: pointer;
    }
    &__img {
      width: 180px;
      position: absolute;
      top: 40%;
      left: -3rem;
    }
  }

  .show-menu {
    top: 0;
  }

  .bg-header {
    background-color: transparent;
    &::after {
      content: "";
      position: absolute;
      width: 1000%;
      height: 100%;
      background-color: rgba(20, 22, 26, 0.3);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      top: 0;
      left: 0;
      z-index: -1;
    }
  }

  .active-link {
    color: var(--first-color);
  }
`;
