$.fn.datepicker.dates['es'] = {
  days:["Domingo","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"],
  daysShort:["Dom","Lun","Mar","Mié","Jue","Vie","Sáb"],
  daysMin:["Do","Lu","Ma","Mi","Ju","Vi","Sa"],
  months:["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],
  monthsShort:["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"],
  today:"Hoy",
  monthsTitle:"Meses",
  clear:"Borrar",
  weekStart:1,
  format:"dd/mm/yyyy"
};

$('.mammoft-date').datepicker({
    startDate: "1/1/1900",
    endDate: "1/1/3000",
    assumeNearbyYear: true,
    autoclose: true,
    todayHighlight: true,
    format: "dd/mm/yyyy",
    language: "es"
});
