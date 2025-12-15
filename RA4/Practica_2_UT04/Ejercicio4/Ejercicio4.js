class Celular {
  constructor(
    color,
    peso,
    resolucion_pantalla,
    resolucion_camara,
    memoria,
    puedeCargaContacto,
    tiene6G
  ) {
    this.color = color;
    this.peso = peso;
    this.resolucion_pantalla = resolucion_pantalla;
    this.resolucion_camara = resolucion_camara;
    this.memoria = memoria;
    this.puedeCargaContacto = puedeCargaContacto;
    this.tiene6G = tiene6G;
  }

  encender() {
    return "El celular está encendido y listo.";
  }
  reiniciar() {
    return "El celular se está reiniciando...";
  }
  apagar() {
    return "El celular está apagado.";
  }
  tomarFotos() {
    return `Fotos de alta calidad tomadas con ${this.resolucion_camara}.`;
  }
  grabarPantalla() {
    return "Grabación de pantalla iniciada con éxito.";
  }

  compartirCarga() {
    if (this.puedeCargaContacto) {
      return "<p class='method-output tiene'>SÍ: Puede compartir carga por contacto (Wireless PowerShare).</p>";
    } else {
      return "<p class='method-output no_tiene'>NO: No tiene soporte para compartir carga por contacto.</p>";
    }
  }

  conectividad6G() {
    if(this.tiene6G){
      
      return "<p class='method-output tiene'>SÍ: Compatible con conectividad 6G (¡A prueba de futuro!).</p>";

    }else{
      
      return  "<p class='method-output no_tiene'>NO: Conectividad limitada a 5G/4G.</p>";

    }
  }
}

const celularA = new Celular(
  "Azul",
  250,
  "2532 x 1170 px",
  "48 MP Principal + 12 MP Ultra Gran Angular",
  8,
  true,
  false
);
const celularB = new Celular(
  "Rojo",
  400,
  "1920 x 1080 px",
  "60 MP Principal + 12 MP Ultra Gran Angular",
  24,
  true,
  true
);
const celularC = new Celular(
  "Verde",
  370,
  "1920 x 1080 px",
  "48 MP Principal + 12 MP Ultra Gran Angular",
  12,
  false,
  false
);

elementos = new Array(celularA, celularB, celularC);

function mostrarDatos() {
  const moviles = document.getElementById("moviles");

  moviles.innerHTML = "";

  elementos.forEach((movil) => {
    moviles.innerHTML += `<div class='movil'><h3>Especificaciones Técnicas</h3>
                    <ul>
                        <li><span>Color:</span> ${movil.color}</li>
                        <li><span>Peso:</span> ${movil.peso} gramos</li>
                        <li><span>Pantalla:</span> ${
                          movil.resolucion_pantalla
                        }</li>
                        <li><span>Cámara:</span> ${movil.resolucion_camara}</li>
                        <li><span>RAM:</span> ${movil.memoria}</li>
                    </ul>
                    
                    <div class='funciones'>
                            <span>Encendido:</span> 
                            <span>${movil.encender()}</span>
                        
                            <span>Reiniciar:</span> 
                            <span>${movil.reiniciar()}</span>

                            <span>Apagar:</span> 
                            <span>${movil.apagar()}</span>

                            <span>Tomar Fotos:</span> 
                            <span>${movil.tomarFotos()}</span>

                            <span>Grabar Pantalla:</span> 
                            <span>${movil.grabarPantalla()}</span>

                            <span>Compartir Carga:</span> 
                            ${movil.compartirCarga()}

                            <span>Conectividad 6G:</span> 
                            ${movil.conectividad6G()}

                    </div>


                    </div>`;
  });
}
