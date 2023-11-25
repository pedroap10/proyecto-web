import React from "react";
import Swal from "sweetalert2";
import withReactContent from "sweetalert2-react-content";

export function show_popup(mensaje, icono, foco) {
    const mySwal = withReactContent(Swal);
    mySwal.fire({
        title: mensaje,
        icon: icono
    });
}

function onfocus(foco) {
    if (foco !== '') {
        document.getElementById(foco).focus();
    }
}