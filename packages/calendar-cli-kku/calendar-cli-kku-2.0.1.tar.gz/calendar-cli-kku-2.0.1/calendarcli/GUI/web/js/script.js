var selectedDate = new Date();
console.log(selectedDate);
jQuery(document).ready(function () {
    jQuery('.datetimepicker').datepicker({
        timepicker: true,
        language: 'en',
        range: true,
        multipleDates: true,
        multipleDatesSeparator: " - "
    });
    jQuery("#add-event").submit(function () {
        // alert("Submitted");
        form = $('#add-event')
        var values = {};
        $.each(form.serializeArray(), function (i, field) {
            values[field.name] = field.value;
        });
        if(values['name']==''){
            alert("Please Enter event name.")
        }else{
            jQuery('#modal-view-event-add').modal().modal("toggle");
            eel.addEventGoogle(values)
        }
        return false;
    });
    $('#update-event').submit(function () {
        $('#modal-view-event-update').modal('toggle');
        var form = $('#update-event')
        var values = {};
        $.each(form.serializeArray(), function (i, field) {
            values[field.name] = field.value;
        });
        console.log(values);
        eel.update(values);
    })
});

(function () {
    'use strict';
    // ------------------------------------------------------- //
    // Calendar
    // ------------------------------------------------------ //
    jQuery(function () {
        // page is ready
        jQuery('#calendar').fullCalendar({
            eventLimit: true, 
            themeSystem: 'bootstrap4',
            businessHours: false,
            defaultView: 'month',
            editable: true,
            header: {
                left: 'title',
                center: 'month,agendaWeek,agendaDay',
                right: 'today prev,next'
            },
            dayClick: function () {
                jQuery('#modal-view-event-add').modal();
                selectedDate = new Date($(this).attr('data-date'))
                var picker = $('.datetimepicker').data('datepicker');
                picker.clear()
                picker.selectDate(selectedDate)

            },
            eventClick: function (event, jsEvent, view) {
                jQuery('.event-title').html(`<a href='${event.GoogleCalendarUrl}' target="_blank" style="color: #000;">${event.title}</a>`);
                jQuery('.event-body').html(`${event.description}</br>${event.location?'@ ':''}${event.location}`);
                jQuery('#modal-view-event').modal().modal("toggle");
                $('#deleteeventbtn').click(function () {
                    deleteEvent(event.guuid);
                    $('#calendar').fullCalendar('removeEvents',event._id);
                    jQuery('#modal-view-event').modal().modal("toggle");
                })
                $('#editeventbtn').click(function () {
                    $('#modal-view-event').modal('toggle');
                    $('#modal-view-event-update').modal('toggle');
                    console.log(event);
                    var form = $('#update-event')
                    form[0][0].value = event.title;
                    form[0][1].value = event.description;
                    form[0][2].value = event.location;
                    form[0][3].value = event.guuid;
                })
            },
            eventDrop: function (event, delta, revertFunc) {
                // console.log(event);
                updateEventToGoogle(event)
            },
            eventResize: function (event, delta, revertFunc) {
                updateEventToGoogle(event)
            },
            viewRender: function (event, element) {
                clearEvent();
                var date = event.dateProfile.date
                // console.log(date)
                clearTimeout(load)
                load = setTimeout(function () {eel.getEventSourcesGoogle(date.year(),date.month()+1,date.date())},loadEventLag)
                // eel.getEventSourcesGoogle(date.year(),date.month()+1,date.date())

            }
        })
    });
})(jQuery);

var load
var loadEventLag = 300



eel.expose(loadingProgressBarShow);
function loadingProgressBarShow() { $('.spinner-container').addClass('loading'); }

eel.expose(loadingProgressBarHide);
function loadingProgressBarHide() { a = $('.spinner-container').removeClass('loading'); }


eel.expose(addEventToCalendar)
function addEventToCalendar(events,clear = true) {
    if(clear){
        clearEvent();
    }
    var calendar = $('#calendar').fullCalendar();
    calendar.data('fullCalendar').addEventSource(events)
    moreCell = $('.fc-more-cell')
    if (moreCell[0])
        moreCell.click(function () {
            $('.fc-more-popover').css('background', '#eee')
        })
}

function clearEvent() {
    calendar = $('#calendar').fullCalendar().data('fullCalendar');
    calendar = calendar.eventManager.removeAllSources()
}


function updateEventToGoogle(event) {
    console.log('updatting');
    eel.moveEventGoogle(event.guuid,event.start,event.end,event.allDay)
}


function deleteEvent(id){
    eel.delete(id)
}