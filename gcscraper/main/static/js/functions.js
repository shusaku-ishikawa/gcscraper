

function update_page_order(order_str) {
    return $.ajax({
        url: UPDATE_PAGE_ORDER,
        type: 'POST',
        dataType: 'json',
        data: {
            order_str: order_str
        }
    });
}
function add_new_page(insert_at) {
    return $.ajax({
        url: ADD_NEW_PAGE,
        type: 'POST',
        dataType: 'json',
        async: true,
        data: {
            insert_at: insert_at
        },
    });
}
function delete_page(pk) {
    return $.ajax({
        url: DELETE_PAGE,
        type: 'POST',
        dataType: 'json',
        async: true,
        data: {
            pk: pk
        },
    });
}
function update_page_field(pk, field_name, field_value) {
    return $.ajax({
        url: UPDATE_PAGE_FIELD,
        type: 'POST',
        dataType: 'json',
        async: true,
        data: {
            pk: pk,
            field_name : field_name,
            field_value: field_value
        },
    });
}

function get_all_pages() {
    return $.ajax({
        url: GET_ALL_PAGES,
        type: 'GET',
        dataType: 'json',
        async: true,
    });
}
function add_to_group(group_id, code) {
    return $.ajax({
        url: ADD_TO_GROUP,
        type: 'POST',
        dataType: 'json',
        async: true,
        data: {
            group_id: group_id,
            code: code
        }
    });
}

function delete_from_group(pagegroup_id) {
    return $.ajax({
        url: DELETE_FROM_GROUP,
        type: 'POST',
        dataType: 'json',
        async: true,
        data: {
            pagegroup_id: pagegroup_id
        }
    });
}
function update_pagegroup_order(group_id, new_order) {
    return $.ajax({
        url: UPDATE_PAGEGROUP_ORDER,
        type: 'POST',
        dataType: 'json',
        async: true,
        data: {
            group_id: group_id,
            new_order: new_order
        },
    });
}
function update_group_order(new_order) {
    return $.ajax({
        url: UPDATE_GROUP_ORDER,
        type: 'POST',
        dataType: 'json',
        async: true,
        data: {
            
            new_order: new_order
        },
    });
}

function update_group_memo(group_id, memo) {
    return $.ajax({
        url: UPDATE_GROUP_MEMO,
        type: 'POST',
        dataType: 'json',
        async: true,
        data: {
            group_id: group_id,
            memo: memo
        },
    });
}

function add_new_group(after) {
    return $.ajax({
        url: ADD_NEW_GROUP,
        type: 'POST',
        dataType: 'json',
        async: true,
        data: {
            after: after
        },
    });
}
function delete_group(group_id) {
    return $.ajax({
        url: DELETE_GROUP,
        type: 'POST',
        dataType: 'json',
        async: true,
        data: {
            group_id: group_id
        },
    });
}
function update_group_field(group_id, field_name, field_value) {
    return $.ajax({
        url: UPDATE_GROUP_FIELD,
        type: 'POST',
        dataType: 'json',
        async: true,
        data: {
            group_id: group_id,
            field_name: field_name,
            field_value: field_value
        },
    });
}
function init_page_sortable() {
    $( ".nested" ).sortable({
        update: function(event, ui) {
            
            var updatedInfo =  $('.nested').sortable("toArray").join(",");
            update_page_order(updatedInfo)
            .done(function(res) {
                if (res.error) {
                    alert(res.error);
                    return false;
                } else if (res.success) {
                    console.log('success');
                }

            })
            .fail(function(data, textStatus, xhr) {
                if (data.status == 401) {
                    window.location.href = BASE_URL_LOGIN;
                }
                alert('error');
            });
        }
    });
    $( ".nested" ).disableSelection();
}
function init_pagegroup_sortable() {
    $( ".nested-p" ).sortable({
        update: function(event, ui) {
            var group_id = $(this).closest('li.group-li').attr('id');
            var new_order =  $(this).sortable("toArray").join(",");
            update_pagegroup_order(group_id, new_order)
            .done(function(res) {
                if (res.error) {
                    alert(res.error);
                    return false;
                } else if (res.success) {
                    console.log('success');
                }

            })
            .fail(function(data, textStatus, xhr) {
                if (data.status == 401) {
                    window.location.href = BASE_URL_LOGIN;
                }
                alert('error');
            });
        }
    });
    $( ".nested-p" ).disableSelection();
}
function init_group_sortable() {
    $( ".nested-g" ).sortable({
        update: function(event, ui) {
            var group_id = $(this).closest('li.group-li').attr('id');
            var new_order =  $(this).sortable("toArray").join(",");
            update_group_order(new_order)
            .done(function(res) {
                if (res.error) {
                    alert(res.error);
                    return false;
                } else if (res.success) {
                    console.log('success');
                }

            })
            .fail(function(data, textStatus, xhr) {
                if (data.status == 401) {
                    window.location.href = BASE_URL_LOGIN;
                }
                alert('error');
            });
        }
    });
    $( ".nested-g" ).disableSelection();
}