function onNext(parent, panel) {
  hash = "#" + panel.id;
  $(".acc-wizard-sidebar",$(parent))
      .children("li")
      .children("a[href='" + hash + "']")
      .parent("li")
      .removeClass("acc-wizard-todo")
      .addClass("acc-wizard-completed");
}

$(function() {

	$(".acc-wizard").accwizard({onNext:onNext});

    $('#projectionDate').datetimepicker({
    	format:'MMMM Do YYYY',
    }).on('dp.change', function(e) {
    	
    });

});