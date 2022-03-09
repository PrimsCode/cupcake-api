const BASE_URL="http://127.0.0.1:5000";

function createCupcake(cupcake){
    const upperName = cupcake.flavor.toUpperCase();
    let recipe = cupcake.recipe;

    if (recipe == null){
        recipe = "https://media-cldnry.s-nbcnews.com/image/upload/newscms/2016_33/1152133/cupcake-stock2-today-160819-tease.jpg"
    }

    return `
    <div class="containter border border-2 rounded-2 w-25" style="background-color:white" id='${cupcake.id}'>
        <div class="row justify-content-center text-center" id='${cupcake.id}'>
            <div class="column p-3" id='${cupcake.id}'>
                <a href="${recipe}">
                    <img src="${cupcake.image}" alt="${cupcake.flavor}" class="img-fluid rounded-lg" style="width:200px; height:200px; object-fit:cover">
                </a>
                <h5>${upperName}</h5>
                <p><b>Size:</b> ${cupcake.size}</p>
                <p><b>Rating:</b> ${cupcake.rating}</p>
                <button id="delete-button" class="btn btn-danger" data-id='${cupcake.id}'>X</button>
            </div>
        </div>
    </div>
    `
}

function showTopCupcake(cupcake){
    const upperName = cupcake.flavor.toUpperCase()
        return `        
        <div class="col border border-2 rounded-2 w-25 text-center" style="background-color:white" id='${cupcake.id}'>
        <h2>Highest Rated Cupcake</h2>
            <div class="row justify-content-center text-center" id='${cupcake.id}'>
                <div class="column p-3" id='${cupcake.id}'>            
                    <img src="${cupcake.image}" alt="${cupcake.flavor}" class="img-fluid rounded-lg" style="width:400px; height:400px; object-fit:cover">
                    <h3>${upperName}</h3>
                </div>
            </div>
        </div>
        `
    }

async function topCupcake(){
    const res = await axios.get(`${BASE_URL}/cupcakes`);

    for (let cupcakeData of res.data.cupcakes){
        if (cupcakeData.rating == 10){
            let topCupcakeData = cupcakeData;
            let topCupcake = $(showTopCupcake(topCupcakeData));
            $('#top-cupcake').append(topCupcake);
            return;
        }
    }
}

async function showCupcakes(){
    const res = await axios.get(`${BASE_URL}/cupcakes`);

    for (let cupcakeData of res.data.cupcakes){
        let cupcake = $(createCupcake(cupcakeData));
        $('#cupcakes-display').append(cupcake)
    }
}


$('#add-cupcake-form').on('submit', async function(e){
    e.preventDefault();

    let flavor = $('#flavor').val();
    let size = $('#size').val();
    let rating = $('#rating').val();
    let image = $('#image').val();
    let recipe = $('#recipe').val();

    const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, {flavor, size, rating, image, recipe});
    let newCupcake = $(createCupcake(newCupcakeResponse.data.cupcake));
    $("#cupcakes-display").append(newCupcake);
    $("#add-cupcake-form").trigger('reset');
});

$('#cupcakes-display').on('click', '#delete-button', async function(e){
    e.preventDefault();

    const id = $(this).data('id');
    await axios.delete(`${BASE_URL}/cupcakes/${id}`)
    $(`#${id}`).remove();
})



$(showCupcakes);
$(topCupcake);

