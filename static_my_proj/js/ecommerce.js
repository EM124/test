$(document).ready(function(){ 
	//HOME
	$( "#datepicker" ).datepicker();
	$( "#datepicker2" ).datepicker();
	var payrollForm = $(".payroll_table")
	var globalTaxes = $(".global_taxes")
	var count=0
	//"<td><input id='payement_proof_"+item.pk+"' type='file'><td>"+

						// $.alert({
						// 	title: "Oops!",
						// 	content: msg,
						// 	theme: "modern"
						// })	
	//DAYCARE CREATE
	if(window.location.pathname=='/daycare/')
	{
			$.ajax({
			method: "GET",
			url: "/daycare/",
			success: function(data){
				//var content = JSON.parse(data)
				console.log(data)
				
				$.each(data, function(i, item) {
					if(i==1){
						$.each(item, function(i, item){	
							$(".unique_company_taxes").append('<div class="row '+i+'_class"><div class="col-4"><input type="text" name="unique_company" placeholder="'+i+'" class="form-control" id="label_'+i+'"></div><div class="col-5"><input type="text" name="unique_company_tax" placeholder="'+i+'" class="form-control" id="'+i+'"></div><div class="col-3 form-group"><button type="button" id="id-'+i+'" class="btn btn-success" style="margin: 10px;"> Delete </button></div></div>')
							$("#"+i).val(item)
							$("#label_"+i).val(i)
						})
					}
					if(i==0){
						$.each(item, function(i, item){	
							$(".unique_employee_taxes").append('<div class="row '+i+'_class"><div class="col-4"><input type="text" name="unique_employee" placeholder="'+i+'" class="form-control" id="label_'+i+'"></div><div class="col-5"><input type="text" name="unique_employee_tax" placeholder="'+i+'" class="form-control" id="'+i+'"></div><div class="col-3 form-group"><button type="button" id="id-'+i+'" class="btn btn-success" style="margin: 10px;"> Delete </button></div></div>')
							$("#"+i).val(item)
							$("#label_"+i).val(i)
						})
					}
				})
			},
			error: function(error){
				console.log(error)
			}
		})
	}

	//DAYCARE UPDATE
	var daycare_detail = new RegExp(/\/daycare\/\d+/);
	if(window.location.pathname.match(daycare_detail))
	{
		console.log("2")
		var daycare_id = window.location.pathname.match(/\d+/)
			$.ajax({
			method: "GET",
			url: "/daycare/"+daycare_id+"/",
			success: function(data){
				//var content = JSON.parse(data)
				console.log(data)
				
				$.each(data, function(i, item) {
					if(i==0){
						$.each(item, function(i, item){	
							$(".global_company_taxes").append('<div class="row '+i+'_class"><div class="col-4"><input type="text" name="global_company" placeholder="'+i+'" class="form-control" id="label_'+i+'"></div><div class="col-5"><input type="text" name="global_company_tax" placeholder="'+i+'" class="form-control" id="'+i+'"></div><div class="col-3 form-group"><button type="button" id="id-'+i+'" class="btn btn-success" style="margin: 10px;"> Delete </button></div></div>')
							$("#"+i).val(item)
							$("#label_"+i).val(i)
						})
					}
					if(i==1){
						$.each(item, function(i, item){	
							$(".global_employee_taxes").append('<div class="row '+i+'_class"><div class="col-4"><input type="text" name="global_employee" placeholder="'+i+'" class="form-control" id="label_'+i+'"></div><div class="col-5"><input type="text" name="global_employee_tax" placeholder="'+i+'" class="form-control" id="'+i+'"></div><div class="col-3 form-group"><button type="button" id="id-'+i+'" class="btn btn-success" style="margin: 10px;"> Delete </button></div></div>')
							$("#"+i).val(item)
							$("#label_"+i).val(i)
						})
					}
					if(i==2){
						$.each(item, function(i, item){	
							$(".unique_company_taxes").append('<div class="row '+i+'_class"><div class="col-4"><input type="text" name="unique_company" placeholder="'+i+'" class="form-control" id="label_'+i+'"></div><div class="col-5"><input type="text" name="unique_company_tax" placeholder="'+i+'" class="form-control" id="'+i+'"></div><div class="col-3 form-group"><button type="button" id="id-'+i+'" class="btn btn-success" style="margin: 10px;"> Delete </button></div></div>')
							$("#"+i).val(item)
							$("#label_"+i).val(i)
						})
					}
					if(i==3){
						$.each(item, function(i, item){	
							$(".unique_employee_taxes").append('<div class="row '+i+'_class"><div class="col-4"><input type="text" name="unique_employee" placeholder="'+i+'" class="form-control" id="label_'+i+'"></div><div class="col-5"><input type="text" name="unique_employee_tax" placeholder="'+i+'" class="form-control" id="'+i+'"></div><div class="col-3 form-group"><button type="button" id="id-'+i+'" class="btn btn-success" style="margin: 10px;"> Delete </button></div></div>')
							$("#"+i).val(item)
							$("#label_"+i).val(i)
						})
					}

				})
			},
			error: function(error){
				console.log(error)
			}
		})
	}

	//ADD GLOBAL COMPANY TAX FIELD
	$(".add-global-company-tax").click(function(){
		$(".global_company_taxes").append('<div class="row global_company_tax_'+count+'_class"><div class="col-4"><input type="text" name="global_company" placeholder="new tax" class="form-control"></div><div class="col-5"><input type="text" name="global_company_tax" placeholder="new tax" class="form-control"></div><div class="col-3 form-group"><button type="button" id="new-global_company_tax_'+count+'" class="btn btn-success" style="margin: 10px;"> Delete </button></div></div>')
		count++
	})
	
	//ADD GLOBAL EMPLOYEE TAX FIELD
	$(".add-global-employee-tax").click(function(){
		$(".global_employee_taxes").append('<div class="row global_employee_tax_'+count+'_class"><div class="col-4"><input type="text" name="global_employee" placeholder="new tax" class="form-control"></div><div class="col-5"><input type="text" name="global_employee_tax" placeholder="new tax" class="form-control"></div><div class="col-3 form-group"><button type="button" id="new-global_employee_tax_'+count+'" class="btn btn-success" style="margin: 10px;"> Delete </button></div></div>')
		count++
	})
	


	//ADD UNIQUE COMPANY TAX FIELD
	$(".add-unique-company-tax").click(function(){
		$(".unique_company_taxes").append('<div class="row unique_company_tax_'+count+'_class"><div class="col-4"><input type="text" name="unique_company" placeholder="new tax" class="form-control"></div><div class="col-5"><input type="text" name="unique_company_tax" placeholder="new tax" class="form-control"></div><div class="col-3 form-group"><button type="button" id="new-unique_company_tax_'+count+'" class="btn btn-success" style="margin: 10px;"> Delete </button></div></div>')
		count++
	})
	
	//ADD UNIQUE EMPLOYEE TAX FIELD
	$(".add-unique-employee-tax").click(function(){
		$(".unique_employee_taxes").append('<div class="row unique_employee_tax_'+count+'_class"><div class="col-4"><input type="text" name="unique_employee" placeholder="new tax" class="form-control"></div><div class="col-5"><input type="text" name="unique_employee_tax" placeholder="new tax" class="form-control"></div><div class="col-3 form-group"><button type="button" id="new-unique_employee_tax_'+count+'" class="btn btn-success" style="margin: 10px;"> Delete </button></div></div>')
		count++
	})

	//DELETE UNIQUE COMPANY TAX FIELD
	$(".unique_company_taxes").click(function(e){
		if(e.target.type=="button")
		{
			var idClicked = e.target.id
			var id= idClicked.split("-")
			$("."+id[1]+"_class").remove()
			
		}
	})
	
	//DELETE UNIQUE EMPLOYEE TAX FIELD
	$(".unique_employee_taxes").click(function(e){
		if(e.target.type=="button")
		{
			var idClicked = e.target.id
			var id= idClicked.split("-")
			$("."+id[1]+"_class").remove()
			
		}
	})
	//DELETE GLOBAL COMPANY TAX FIELD
	$(".global_company_taxes").click(function(e){
		if(e.target.type=="button")
		{
			var idClicked = e.target.id
			var id= idClicked.split("-")
			$("."+id[1]+"_class").remove()
			
		}
	})
	
	//DELETE GLOBAL EMPLOYEE TAX FIELD
	$(".global_employee_taxes").click(function(e){
		if(e.target.type=="button")
		{
			var idClicked = e.target.id
			var id= idClicked.split("-")
			$("."+id[1]+"_class").remove()
			
		}
	})



	//PAYROLL

	var $rows = $('.user-payroll-table tr');
	$('#filter').keyup(function() {

		var val = '^(?=.*\\b' + $.trim($(this).val()).split(/\s+/).join('\\b)(?=.*\\b') + ').*$',
		reg = RegExp(val, 'i'),
		text;

		$rows.show().filter(function() {
			text = $(this).text().replace(/\s+/g, ' ');
			return !reg.test(text);
		}).hide();
	});
	$('.user-payroll-table tr').click(function() {
		var id_row = $(this).find("td").attr("name");
		$.ajax({
			method: "GET",
			url: "/payrolls/",
			data: {'id': id_row},
			success: function(data){
				var content = JSON.parse(data)
				$(".parent-full-name").empty()
				$(".user-address").empty()
				$(".child-full-name").empty()
				$("#payroll-body-list").empty()
				$.each(content, function(i, item) {
    				if(item.model == "accounts.user")
    				{
    					$(".parent-full-name").append(item.fields.adult_first_name + " " + item.fields.adult_last_name)
    					$(".parent-full-name").attr('id', id_row) 
    					$(".adult_full_name").empty()
	    				$(".adult_full_name").append(item.fields.adult_first_name + " " + item.fields.adult_last_name)
    				}
    				if(item.model == "addresses.address")
    				{
    					$(".user-address").append(item.fields.address_line_1 + " " + item.fields.address_line_2 + "</br>" +
    							item.fields.city +", " + item.fields.province + ", " + item.fields.country + "</br>" +
    							item.fields.postal_code + "</br>" + item.fields.cell_phone + "</br>" + item.fields.home_phone)
    				}
    				if(item.model == "kids.kid")
    				{
    					$(".child-full-name").append(item.fields.child_first_name + " " + item.fields.child_last_name + "</br>")
    				}
    				if(item.model == "payroll.payroll")
    				{
    					var from= item.fields.from_time.split("T")
    					var to= item.fields.to_time.split("T")
    					if(item.fields.payed == false){
    						$("#payroll-body-list").append("<tr>"+
    						"<td>" + from[0] + "</td>"+
    						"<td>" + to[0] + "</td>"+
    						// "<td><input type='checkbox' id='" +item.pk + "'/></td>"+
    						"<td><a href='/payrolls/"+item.pk+"'><button style='width:100%' type='button' class='btn btn-default' data-dismiss='modal' role='button'>View</button></a></td>"+
    						"</tr>")
    					}
    					else {
    						$("#payroll-body-list").append("<tr>"+
    						"<td>" + from[0] + "</td>"+
    						"<td>" + to[0] + "</td>"+
    						//"<td><input type='checkbox' id='" +item.pk + "' checked/></td>"+
    						"<td><a href='/payrolls/"+item.pk+"'><button style='width:100%' type='button' class='btn btn-default' data-dismiss='modal' role='button'>View</button></a></td>"+
    						"</tr>")
    					}
    				}
    				
  				})
				payrollForm = $(".payroll_table")
				console.log(content)
			},
			error: function(error){
				console.log(error)
			}
		})
	});

	//ADD A PAYROLL
	$('#refresh-payroll').click(function() {
		date1 = $("#datepicker").datepicker().val()
		date2 = $("#datepicker2").datepicker().val()
		id_user = $(".parent-full-name").attr('id')
		$.ajax({
			method: "POST",
			url: "/payrolls/add-payroll/",
			data: {'id': id_user, 'date1': date1, 'date2': date2},
			success: function(data){
				console.log(data)
				//var content = JSON.parse(data)
				$('.company_table').empty()
				$('.employee_table').empty()
				$('#rate').val('')
				$('#hours').val('')
				$.each(data, function(i, item) {
    				if(i==0)
    				{
	    				 $("#rate").val(item.salary)
	    				 $("#hours").val(item.hours)
    				}
 					if(i==1)
 					{
 						$.each(item, function(i, item){

 							if(i == "Vacation_Pay")
 							{
 								$('#vacationAccrued').val(parseFloat(item.Current))
 							}
 							$('.company_table').append('<tr>'+
 								'<td>' + i + '</td>' +
 								'<td>' +
 								'<div class="form-group">' +
 								'<input type="text" id="'+i+'_Current" name="company_tax" class="input-sm form-control">' +
 								'</div>' +
 								'</td>' +
 								'<td>'+
 								'<div class="form-group">' +
 								'<input type="text" id="'+i+'_YTD" name="company_tax" class="input-sm form-control">' +
 								'</div>' +
 								'</td>' +
 								'</tr>'
 								)
 							$("#"+i+"_Current").val(item.Current)
 							$("#"+i+"_YTD").val(item.YTD)

 						})
 					}
 					if(i==2)
 					{

 						$.each(item, function(i, item){

 							if(i!="Cheque_Amount"){
 								$('.employee_table').append('<tr>'+
 									'<td>' + i + '</td>' +
 									'<td>' +
 									'<div class="form-group">' +
 									'<input type="text" id="'+i+'_Current" name="employee_tax" class="input-sm form-control">' +
 									'</div>' +
 									'</td>' +
 									'<td>'+
 									'<div class="form-group">' +
 									'<input type="text" id="'+i+'_YTD" name="employee_tax" class="input-sm form-control">' +
 									'</div>' +
 									'</td>' +
 									'</tr>'
 									)
 								$("#"+i+"_Current").val(item.Current)
 								$("#"+i+"_YTD").val(item.YTD)
 							}else{
 								$(".cheque_amount").val(item)
 							}

 						})
 					}
  				})
	
			},
			error: function(error){
				console.log(error)
			}
		})
	});

	//SAVE PAYROLL
		$('#savePayroll').click(function() {
		date1 = $("#datepicker").datepicker().val()
		date2 = $("#datepicker2").datepicker().val()
		id_user = $(".parent-full-name").attr('id')
		company_taxes = getCompanyTaxes()
		employee_taxes = getEmployeeTaxes()
		cheque_amount = $(".cheque_amount").val()
		hours = $("#hours").val()
		$.ajax({
			method: "POST",
			url: "/payrolls/save-payroll/",
			data: {'id': id_user, 'date1': date1, 
			'date2': date2, 
			'company_taxes': JSON.stringify(company_taxes), 
			'employee_taxes': JSON.stringify(employee_taxes),
			'cheque_amount': cheque_amount,
			'hours': hours},
			success: function(data){
				var content = JSON.parse(data)
				$.each(content, function(i, item) {
    				if(item.model == "payroll.payroll")
    				{
    					var from= item.fields.from_time.split("T")
    					var to= item.fields.to_time.split("T")

    					$("#payroll-body-list").append("<tr>"+
    						"<td>" + from[0] + "</td>"+
    						"<td>" + to[0] + "</td>"+
    						//"<td><input type='checkbox' id='" +item.pk + "' checked/></td>"+
    						"<td><a href='/payrolls/"+item.pk+"'><button style='width:100%' type='button' class='btn btn-default' data-dismiss='modal' role='button'>View</button></a></td>"+
    						"</tr>")
    					$('#payroll-modal').modal('toggle');
    					
    				}
  				})
				console.log(content)
				payrollForm = $(".payroll_table")
	
			},
			error: function(error){
				console.log(error)
			}
		})
	});

	function getCompanyTaxes()
	{
		company_taxes={}

		$('.company_table tr').each(function() {
        var values = [];
        values.push($(this)[0].textContent)
        $(this).find("input").each(function(){
			values.push($(this).val())
        });
        company_taxes[values[0]]={"Current":values[1],"YTD":values[2]}
    	});

		return company_taxes
	}
	
	function getEmployeeTaxes()
	{
		employee_taxes={}

		$('.employee_table tr').each(function() {
        var values = [];
        values.push($(this)[0].textContent)
        $(this).find("input").each(function(){
			values.push($(this).val())
        });
        employee_taxes[values[0]]={"Current":values[1],"YTD":values[2]}
    	});

		return employee_taxes
	}


	//PAYROLL DETAIL PAGE
	var path = new RegExp(/\/payrolls\/\d+/);
	if(window.location.pathname.match(path))
	{
		var payroll_id = window.location.pathname.match(/\d+/)
		$.ajax({
				method: "GET",
				url: "/payrolls/"+payroll_id+"/",
				success: function(data){
					var content = JSON.parse(data)
					console.log(content)

					$.each(content, function(i, item) {
    				if(item.model == "accounts.user")
    				{
    					//$(".adult_full_name").empty()
    					//$(".adult_full_name").append(item.fields.adult_first_name + " " + item.fields.adult_last_name)
    					$("#rate").val(item.fields.salary) 
    				}
    				if(item.model == "worklogs.worklog")
    				{
    					$("#hours").val(item.fields.hours)
    				}
    				if(item.model == "payroll.payroll")
    				{
    					var employee_taxes = JSON.parse(item.fields.employee_taxes)
    					var company_taxes = JSON.parse(item.fields.company_taxes)
    					$(".cheque_amount").val(parseFloat(item.fields.amount_cheque))
						$("#hours").val(parseFloat(item.fields.hours))
						$('#vacationAccrued').val(parseFloat(company_taxes.Vacation_Pay.Current))
    					//employee table
 						$.each(employee_taxes, function(i, item){

 								$('.employee_table').append('<tr>'+
 									'<td>' + i + '</td>' +
 									'<td>' +
 									'<div class="form-group">' +
 									'<input type="text" id="'+i+'_Current" name="employee_tax" class="input-sm form-control">' +
 									'</div>' +
 									'</td>' +
 									'<td>'+
 									'<div class="form-group">' +
 									'<input type="text" id="'+i+'_YTD" name="employee_tax" class="input-sm form-control">' +
 									'</div>' +
 									'</td>' +
 									'</tr>'
 									)
 							$("#"+i+"_Current").val(item.Current)
 							$("#"+i+"_YTD").val(item.YTD)

 						})    					
 						
 						//company table
 						$.each(company_taxes, function(i, item){


 							$('.company_table').append('<tr>'+
 								'<td>' + i + '</td>' +
 								'<td>' +
 								'<div class="form-group">' +
 								'<input type="text" id="'+i+'_Current" name="company_tax" class="input-sm form-control">' +
 								'</div>' +
 								'</td>' +
 								'<td>'+
 								'<div class="form-group">' +
 								'<input type="text" id="'+i+'_YTD" name="company_tax" class="input-sm form-control">' +
 								'</div>' +
 								'</td>' +
 								'</tr>'
 								)
 							$("#"+i+"_Current").val(item.Current)
 							$("#"+i+"_YTD").val(item.YTD)

 						})
						if(item.fields.payed == false){
    						$(".payement").append("<input type='checkbox' id='" +item.pk + "'/>")
    					}
    					else {
    						$(".payement").append("<input type='checkbox' id='" +item.pk + "' checked/>")

    					}
    				}
					})
				},
				error: function(error){
					console.log(error)
				}
			})
	}
	//PAYED PAYROLL
	payrollForm.click(function(e){
		var idClicked = e.target.id;
		if(e.target.type=="checkbox")
		{
				$.ajax({
				method: "POST",
				url: "/payrolls/payroll_payed/",
				data: {'id': idClicked, 'checkbox': $('#'+idClicked).prop('checked')},
				success: function(data){
					//var content = JSON.parse(data)
	    			$.alert({
						title: "Success!",
						content: "Payed has been sucessfully updated",
						theme: "modern"
						})

					payrollForm = $(".payroll_table")
		
				},
				error: function(error){
					console.log(error)
				}
			})
		}
	});

	//CREATE,UPDATE,DELETE USERS
	$(".add-kid").click(function(){
		$(".add-kid-append").append('<label for="id_child_first_name">First Name:</label><input type="text" name="child_first_name" class="form-control" placeholder="child first name" id="id_child_first_name" name="child_first_name" /><label for="id_child_last_name">Full Name:</label><input type="text" name="child_last_name" class="form-control" placeholder="child last name" id="id_child_last_name" name="child_last_name" /><label for="id_gender">Gender:</label><select name="gender" class="form-control" id="id_gender" name="gender"><option value="M" selected>Male</option><option value="F">Female</option></select>');
	});

	$(".add-kid-update").click(function(){
		$(".add-kid-append-update").append('<label for="id_child_first_name">First Name:</label><input type="text" name="child_first_name" class="form-control" placeholder="child first name" id="id_child_first_name" name="child_first_name" /><label for="id_child_last_name">Full Name:</label><input type="text" name="child_last_name" class="form-control" placeholder="child last name" id="id_child_last_name" name="child_last_name" /><label for="id_gender">Gender:</label><select name="gender" class="form-control" id="id_gender" name="gender"><option value="M" selected>Male</option><option value="F">Female</option></select>');
	});

	$("button").click(function(e){
		var idClicked = e.target.id;

		if(idClicked.indexOf("-Child") != -1){

			$("."+idClicked).remove()
		}
	});

});

	// })


			// Contact Form Handler

			// var contactForm = $(".contact-form")
			// var contactFormMethod = contactForm.attr("method")
			// var contactFormEndPoint = contactForm.attr("action")

			
			// function displaySubmitting(submitBtn, defautlText, doSubmit){
				
			// 	if(doSubmit)
			// 	{
			// 		submitBtn.addClass("disabled")
			// 		submitBtn.html("<i class='fa fa-spin fa-spinner'></i> Sending...")
			// 	} else {
			// 		submitBtn.removeClass("disabled")
			// 		submitBtn.html(defautlText)
			// 	}

			// }
			
			// contactForm.submit(function(event){
			// 	event.preventDefault()
			
			// 	var contactFormSubmitBtn = contactForm.find("[type='submit']")
			// 	var contactFormSubmitBtnTxt = contactFormSubmitBtn.text()

			// 	var contactFormData = contactForm.serialize()
			// 	var thisForm = $(this)
			// 	displaySubmitting(contactFormSubmitBtn, "", true)
			// 	$.ajax({
			// 		method: contactFormMethod,
			// 		url: contactFormEndPoint,
			// 		data: contactFormData,
			// 		success: function(data){
			// 			contactForm[0].reset()
			// 			$.alert({
			// 				title: "Success!",
			// 				content: data.message,
			// 				theme: "modern"
			// 			})
			// 			setTimeout(function(){
			// 				displaySubmitting(contactFormSubmitBtn, contactFormSubmitBtnTxt, false)
			// 			}, 500)
			// 		},
			// 		error: function(error){
			// 			var jsonData = error.responseJSON
			// 			var msg = ""

			// 			$.each(jsonData, function(key, value){
			// 				msg += key + ": " + value[0].message + "<br/>"
			// 			})

			// 			$.alert({
			// 				title: "Oops!",
			// 				content: msg,
			// 				theme: "modern"
			// 			})
			// 			setTimeout(function(){
			// 				displaySubmitting(contactFormSubmitBtn, contactFormSubmitBtnTxt, false)
			// 			}, 500)
			// 		}
			// 	})
			// })





			// // Auto Search
			// var searchForm = $(".search-form")
			// var searchInput = searchForm.find("[name='q']")
			// var typingTimer;
			// var typingInterval = 500
			// var searchBtn = searchForm.find("[type='submit']")

			// searchInput.keyup(function(event){
			// 	clearTimeout(typingTimer)
			// 	typingTimer = setTimeout(performSearch, typingInterval)
			// })

			// searchInput.keydown(function(event){
			// 	clearTimeout(typingTimer)
			// })

			// function doSearch(){
			// 	searchBtn.addClass("disabled")
			// 	searchBtn.html("<i class='fa fa-spin fa-spinner'></i> Searching...")					
			// }

			// function performSearch(){
			// 	doSearch()
			// 	var query = searchInput.val()
			// 	setTimeout(function(){
			// 		window.location.href='/search/?q=' + query
			// 	}, 1000)
			
			// }


			// // Cart + Add Products
			// var productForm = $(".form-product-ajax")

			// productForm.submit(function(event){
			// 	event.preventDefault();
			// 	var thisForm = $(this)
			// 	//var actionEndpoint = thisForm.attr("action");
			// 	var actionEndpoint = thisForm.attr("data-endpoint");
			// 	var httpMethod = thisForm.attr("method");
			// 	var formData = thisForm.serialize();

			// 	$.ajax({
			// 		url: actionEndpoint,
			// 		method: httpMethod,
			// 		data: formData,
			// 		success: function(data){
			// 			var submitSpan = thisForm.find(".submit-span")
			// 			if (data.added){
			// 				submitSpan.html("In cart <button type='submit' class='btn btn-link'>Remove?</button>")
			// 			} else {
			// 				submitSpan.html("<button type='submit' class='btn btn-success'>Add to cart</button>")
			// 			}

			// 			var navbarCount = $(".navbar-cart-count")
			// 			navbarCount.text(data.cartItemCount)
			// 			var currentPath = window.location.href
			// 			if(currentPath.indexOf("cart") != -1)
			// 			{
			// 				refreshCart()
			// 			}
			// 		},
			// 		error: function(errorData){
			// 			$.alert({
			// 				title: "Oops!",
			// 				content: "An error occured",
			// 				theme: "modern"
			// 			})
			// 		}
			// 	})
			// })

			// function refreshCart(){				
			// 	var cartTable = $(".cart-table")
			// 	var cartBody = cartTable.find(".cart-body")
			// 	//cartBody.html("<h1>Changed</h1>")
			// 	var productsRow = cartBody.find(".cart-product")
			// 	var currentUrl = window.location.href

			// 	var refreshCartUrl = '/api/cart/';
			// 	var refreshCartMethod = "GET";
			// 	var data ={};

			// 	$.ajax({
			// 		url: refreshCartUrl,
			// 		method: refreshCartMethod,
			// 		data: data,
			// 		success: function(data){

			// 			var hiddenCartItemRemoveForm = $(".cart-item-remove-form")
			// 			if (data.products.length > 0)
			// 			{
			// 				productsRow.html("")
			// 				i = data.products.length
			// 				$.each(data.products, function(index, value){
			// 					var newCartItemRemove = hiddenCartItemRemoveForm.clone()
			// 					newCartItemRemove.css("display", "block")
			// 					newCartItemRemove.find(".cart-item-product-id").val(value.id)
			// 					cartBody.prepend("<tr><th scope=\"row\">" + i + "</th><td><a href='"+value.url+"'>" +
			// 						value.name + "</a>" + newCartItemRemove.html() + "</td><td>" + value.price + "</td></tr>")
			// 					i--
			// 				})
			// 				cartBody.find(".cart-subtotal").text(data.subtotal)
			// 				cartBody.find(".cart-total").text(data.total)
			// 			} else {
			// 				window.location.href = currentUrl
			// 			}
			
			// 		},
			// 		error: function(errorData){
			// 			$.alert({
			// 				title: "Oops!",
			// 				content: "An error occured",
			// 				theme: "modern"
			// 			})
			// 		}
			// 	})
			// }