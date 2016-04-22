import copy, datetime, math, random

class MonteCarlo(object):

    def __init__(self, board=None, search_time_interval=2):
        self.board = board
        #from board import Board
        #self.board = Board()
        self.calculation_time = datetime.timedelta(seconds=search_time_interval)
        self.sqrt2 = 1.414

        self.wins, self.plays = {}, {}

    def get_play(self):
        if not self.board.rule.has_feasible_location(): return

        begin, turn = datetime.datetime.utcnow(), 0
        while datetime.datetime.utcnow() - begin < self.calculation_time:
            self.run_simulation()
            turn += 1

        print 'Simulations %d times.' % turn

        return self.run_simulation(get_one=True)

    def run_simulation(self, get_one=False):
        internal_board, visited_states, expand, winner = copy.deepcopy(self.board), set(), True, []
        next_key = (internal_board.rule.get_current_player(), internal_board.rule.get_hashed_state())
        tt = 0
        while True:
            fls, loc, cur_key = internal_board.rule.get_feasible_locations(), (), next_key

            if len(fls) <= 1:
                if len(fls) == 1: loc = fls.pop()
            elif self.plays.get(cur_key):
                log_total, val = math.log(self.plays.get(cur_key)), 0
                for fl in fls:
                    tmp_rule = copy.deepcopy(internal_board.rule)
                    tmp_rule.place(fl)
                    tmp_rule.shift(fl)
                    tmp_key = (tmp_rule.get_current_player(), tmp_rule.get_hashed_state())
                    # Exploitation && Exploration
                    if self.plays.get(tmp_key):
                        tmp_val = (2.0*self.wins[tmp_key]/self.plays[tmp_key]) + self.sqrt2*math.sqrt(log_total/self.plays[tmp_key])
                    else: tmp_val = self.sqrt2*math.sqrt(log_total)
                    del tmp_rule

                    if tmp_val > val:
                        val = tmp_val
                        loc = fl
                if val == 0:
                    loc = random.choice(list(fls))
            else:
                loc = random.choice(list(fls))

            if get_one: return loc

            internal_board.rule.place(loc)
            internal_board.rule.shift(loc)
            next_key = (internal_board.rule.get_current_player(), internal_board.rule.get_hashed_state())
            visited_states.add(next_key)
            if expand and next_key not in self.plays:
                expand = False
                self.plays[next_key] = 0
                self.wins[next_key]  = 0

            if internal_board.is_ending():
                winner = internal_board.rule.get_winner()
                break

            tt += 1
            if tt == 100:
                print "### YAMIEDIE ###", internal_board.rule.get_feasible_locations(), loc
                print internal_board.rule.get_state()
            if tt%100 == 0:
                print sum(internal_board.rule.count()), len(self.plays)

        for ps in visited_states:
            if ps not in self.plays: continue
            self.plays[ps] += 1
            if ps[0] in winner: self.wins[ps] += 1

        del internal_board
