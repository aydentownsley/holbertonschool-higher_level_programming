$.ajax({
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  data: { get_param: 'name' },
  type: 'GET',
  dataType: 'json',
  success: function (data) {
    $('#character').text(data.name);
  }
});
