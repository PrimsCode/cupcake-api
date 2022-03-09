from sqlite3 import connect
from app import app
from models import db, Cupcake, connect_db

connect_db(app)

db.drop_all()
db.create_all()

"""Data by Springboard"""

c1 = Cupcake(
    flavor="cherry",
    size="large",
    rating=5,
)

c2 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=9,
    image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
)

"""Data by Prima Jenkins"""

c3 = Cupcake(
    flavor='galaxy',
    size='medium',
    rating=8,
    image='https://thescranline.com/wp-content/uploads/2021/03/Galaxy-Cupcakes.jpg',
    recipe='https://thescranline.com/galaxy-cupcakes/',
)

c4 = Cupcake(
    flavor='lavender',
    size='small',
    rating=8,
    image='https://i0.wp.com/jennyisbaking.com/wp-1c174-content/uploads/2018/07/DSC00419.jpg?w=1080&ssl=1',
    recipe='https://jennyisbaking.com/2018/07/09/lavender-cupcakes/',
)

c5 = Cupcake(
    flavor='lemon',
    size='medium',
    rating=10,
    image='https://cdn.sallysbakingaddiction.com/wp-content/uploads/2013/04/the-best-lemon-cupcakes-5.jpg',
    recipe='https://sallysbakingaddiction.com/homemade-lemon-cupcakes-with-vanilla-frosting/',
)

c6 = Cupcake(
    flavor='matcha strawberry',
    size='large',
    rating=5.5,
    image='https://keeprecipes.com/sites/keeprecipes/files/78713_1392841622_0.jpg',
    recipe='https://keeprecipes.com/recipe/howtocook/matcha-strawberry-cupcakes',
)

c7 = Cupcake(
    flavor='strawberry',
    size='small',
    rating=7.5,
    image='https://confessionsofabakingqueen.com/wp-content/uploads/2019/06/strawberry-cupcakes-recipe-7-of-10-683x1024.jpg',
    recipe='https://confessionsofabakingqueen.com/strawberry-cupcakes/',
)

c8 = Cupcake(
    flavor='red velvet',
    size='medium',
    rating=8,
    image='https://thescranline.com/wp-content/uploads/2021/03/Red-Velvet-Cupckes.jpg',
    recipe='https://thescranline.com/red-velvet-cupcakes/',
)

c9 = Cupcake(
    flavor='molten cookie dough',
    size='large',
    rating=10,
    image='https://cdn.sallysbakingaddiction.com/wp-content/uploads/2019/10/molten-cookie-dough-cupcakes-3-1024x1536.jpg.webp',
    recipe='https://sallysbakingaddiction.com/molten-cookie-dough-cupcakes/',
)

c10 = Cupcake(
    flavor='margarita',
    size='small',
    rating=8,
    image='https://cdn.sallysbakingaddiction.com/wp-content/uploads/2016/04/margarita-cupcakes-425x638.jpg.webp',
    recipe='https://sallysbakingaddiction.com/margarita-cupcakes/',
)

c11 = Cupcake(
    flavor='vanilla',
    size='medium',
    rating=6.7,
    image='https://cdn.cupcakeproject.com/wp-content/uploads/2011/09/Best-Vanilla-Cupcakes-01.jpg',
    recipe='https://www.cupcakeproject.com/best-vanilla-cupcake-recipe/',
)

c12 = Cupcake(
    flavor='butterscotch',
    size='medium',
    rating=8.5,
    image='https://cdn.cupcakeproject.com/wp-content/uploads/2021/07/Butterscotch-Cupcakes-13.jpg',
    recipe='https://www.cupcakeproject.com/butterscotch-cupcakes/',
)

c13 = Cupcake(
    flavor='tiramisu',
    size='large',
    rating=6.5,
    image='https://cdn.cupcakeproject.com/wp-content/uploads/2021/01/Tiramisu-Cupcakes-17.jpg',
    recipe='https://www.cupcakeproject.com/tiramisu-cupcakes/',
)

c14 = Cupcake(
    flavor='chai latte',
    size='small',
    rating=10,
    image='https://cdn.sallysbakingaddiction.com/wp-content/uploads/2018/09/chai-latte-cupcakes-1024x1536.jpg.webp',
    recipe='https://sallysbakingaddiction.com/chai-latte-cupcakes/',
)

c15 = Cupcake(
    flavor='confetti',
    size='large',
    rating=8,
    image='https://cdn.sallysbakingaddiction.com/wp-content/uploads/2019/03/sprinkle-cupcakes-with-vanilla-buttercream.jpg.webp',
    recipe='https://sallysbakingaddiction.com/confetti-cupcakes/',
)

db.session.add_all([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15])
db.session.commit()