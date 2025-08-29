document.getElementById('studentForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    // Recolectar todos los datos del formulario
    const data = {
        rut: document.getElementById('entry_rut').value,
        nombre: document.getElementById('entry_nombre').value,
        fecha_nacimiento: document.getElementById('entry_fecha_nacimiento').value,
        direccion: document.getElementById('entry_direccion').value,
        colegio_procedencia: document.getElementById('entry_colegio_procedencia').value,
        cursos_repetidos: document.getElementById('entry_cursos_repetidos').value,
        nombre_padre: document.getElementById('entry_nombre_padre')?.value,
        rut_padre: document.getElementById('entry_rut_padre')?.value,
        nombre_madre: document.getElementById('entry_nombre_madre')?.value,
        rut_madre: document.getElementById('entry_rut_madre')?.value,
        nombre_contest_encuesta: document.getElementById('entry_nombre_contest_encuesta')?.value,
        jefe_hogar: document.getElementById('entry_jefe_hogar')?.value,
        vive_hogar: document.getElementById('entry_vive_hogar')?.value,
        titular: document.getElementById('entry_titular')?.value,
        titrut: document.getElementById('entry_titrut')?.value,
        titphone: document.getElementById('entry_titphone')?.value,
        suplente: document.getElementById('entry_suplente')?.value,
        suprut: document.getElementById('entry_suprut')?.value,
        supphone: document.getElementById('entry_supphone')?.value,
        n_hermanos: document.getElementById('entry_n_hermanos')?.value,
        hermanos_estudian: document.getElementById('entry_hermanos_estudian')?.value,
        hermanos_no_estudian: document.getElementById('entry_hermanos_no_estudian')?.value,
        otros_viven: document.getElementById('entry_otros_viven')?.value,
        ocupacion_madre: document.getElementById('entry_ocupacion_madre')?.value,
        ocupacion_jefe: document.getElementById('entry_ocupacion_jefe')?.value,
        psicolog: document.getElementById('entry_psicolog')?.value,
        aprende: document.getElementById('entry_aprende')?.value,
        estudia: document.getElementById('entry_estudia')?.value,
        religion: document.getElementById('entry_religion')?.value,
        pie: document.getElementById('entry_pie')?.value,
        emergencia: document.getElementById('entry_emergencia')?.value,
        domicilio: document.getElementById('entry_domicilio')?.value,
        celular: document.getElementById('entry_celular')?.value,
        enfermedad: document.getElementById('entry_enfermedad')?.value,
        chile_solidario: document.getElementById('chile_solidario_var')?.checked ? 1 : 0,
        presento_certificado: document.getElementById('presento_certificado_var')?.checked ? 1 : 0,
        necesita_PAE: document.getElementById('necesita_PAE_var')?.checked ? 1 : 0,
        figura_pate: document.getElementById('figura_pate_var')?.checked ? 1 : 0,
        fig_aporta_recursos: document.getElementById('fig_aporta_recursos_var')?.checked ? 1 : 0,
        locomocion: document.getElementById('locomocion_var')?.checked ? 1 : 0,
        asistereligion: document.getElementById('asistereligion_var')?.checked ? 1 : 0,
        ano_madre: document.getElementById('selected_ano_madre')?.value,
        ano_jefe: document.getElementById('selected_ano_jefe')?.value,
        curso: document.getElementById('selected_option')?.value,
        letra: document.getElementById('selected_letra')?.value
    };

    // Enviar datos al backend
    const response = await fetch('http://localhost:5000/api/alumno', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });

    if (response.ok) {
        alert('Datos guardados correctamente');
    } else {
        alert('Error al guardar los datos');
    }
});