/*! jQuery v1.12.4 | (c) jQuery Foundation | jquery.org/license */
$(document).ready(function() {
    $('#example').DataTable({
      "scrollY":        "550px",
      "scrollCollapse": true,
      "paging":         true,
      "ordering": false,
      language: {
      processing:     "Traitement en cours...",
      search:         "Фильтр",
      lengthMenu:    "Показать _MENU_ элементов",
      info:           "Показано _START_ из _END_ из _TOTAL_ элементов",
      infoEmpty:      "Показано 0 из 0 из 0 элементов",
      infoFiltered:   "(Отфильтровано из _MAX_ позиций)",
      infoPostFix:    "",
      loadingRecords: "Chargement en cours...",
      zeroRecords:    "Aucun &eacute;l&eacute;ment &agrave; afficher",
      emptyTable:     "Нет данных",
      paginate: {
            first:      "Первый",
            previous:   "Предыдущий",
            next:       "Следующий",
            last:       "Последний"
        },
    }
});
} );
