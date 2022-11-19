#Initialize no 1

class Star_Cinema:

    __hall_list = []

    def entry_hall(self,hall):
        self.__hall_list.append(hall)
        
        

#Initialize no 2


class Hall(Star_Cinema):

    def __init__(self,rows,cols,hall_no):
        self.__seats = {}
        self.__show_list = [] 
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
      
        self.entry_hall(self)

    def __repr__(self) -> str:
        return f'Rows: {self.__rows}, Columns: {self.__cols}, Hall No: {self.__hall_no}'
    
   
   
   # Initialize no 3

    def entry_show(self, movie_id, movie_name, movie_time):
        self.__show_list.append((movie_id, movie_name, movie_time)) 
        hall_seat = [['Empty']*self.__cols for i in range(self.__rows)]
        self.__seats[movie_id] = hall_seat


    #Structure part no 4

    def book_seats(self,customer_name,customer_number,show_id,seat_numbers):

        id = False
        for movie_show_id in self.__seats:
            if movie_show_id == show_id:
                id = True
                break

        if id == False:
            print('Invalid Movie id, Sorry!')
            return

        seat_no = 0
        seat_nums = []

        for idx,val in enumerate(self.__seats[movie_show_id]):
            if type(val) is list:
                siz = len(val)

                seat_nums = len(seat_numbers)
    
                for i in range(siz):
                    seat_nums.append((idx,i))

        
        for m_set in seat_numbers:
            if m_set in seat_nums:
                seat_no+=1

            else:
                print(f'Sorry! Seat No: {m_set[0]+1,m_set[1]+1} Invalid')
                seat_numbers.remove(m_set)


                                         
        if seat_no > 0:

            for tic in seat_numbers:

                if self.__seats[show_id][tic[0]][tic[1]] == 'Empty':
                    self.__seats[show_id][tic[0]][tic[1]] = 'Booked'
                    print(f'Seat No: {tic[0]+1,tic[1]+1} Booked')


                elif self.__seats[show_id][tic[0]][tic[1]] != 'Empty':
                    print(f'Seat No: {tic[0]+1,tic[1]+1} is Already Booked')
     




    #structure part 5

    def view_show_list(self):
        print(self.__show_list) 




    # structure part 6

    def view_available_seats(self,mv_id):
        compairId = False
        for hall_movie_id in self.__seats:
            if hall_movie_id == mv_id:
                compairId = True    

                for idx,val in enumerate(self.__seats[hall_movie_id]):
                    if type(val) is list:
                        siz = len(val)
                        for i in range(siz):
                            if val[i] != 'Booked':
                                seat_no = (idx+1,i+1)
                                print(seat_no,val[i])
                break


        if compairId == False:
            print('Invalid Movie Id, Sorry!')
            return


          

    

        


hall_1 = Hall(3,2,156)


hall_1.entry_show('G19','Dipu No 2','8:30 PM')
hall_1.entry_show('H22','Debi','10:00 PM')





while True:
    print("1.All Shows\n2.Available Seats\n3. Ticket Booked")
    
    viewer_input = int(input('Enter An Option: '))
    if viewer_input == 1:
        hall_1.view_show_list()
    elif viewer_input == 2:
        movie_id = input('Enter Movie Id: ')
        hall_1.view_available_seats(movie_id)
    else:
        movie_seats = []
        customer_name = input('Enter your name: ')
        customer_number = input('Enter your phone number: ')
        movie_id = input('Enter Movie Id: ')
        n = int(input('How many seats you need: '))
        for i in range(n):
            row,col = input('Enter row,col e.g = 1,2 seat number: ').split(',')
            row = int(row)-1
            col = int(col)-1
            seat_tuple = (row,col)
            movie_seats.append(seat_tuple)

        hall_1.book_seats(customer_name,customer_number,movie_id,movie_seats)