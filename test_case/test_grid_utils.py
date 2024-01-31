from grid.grid_utils import is_gridChallenge
import unittest

class GridChallengeTest(unittest.TestCase):
    def test_give_hcd_awc_shm_is_not_grid(self):
        prime_list = ['hcd','awc','shm']
        is_grid = is_gridChallenge(prime_list)
        self.assertEqual(is_grid, 'NO')

    def test_give_erthgf_awc_shm_is_not_grid(self):
        prime_list = ['erthgf','awc','shm']
        is_grid = is_gridChallenge(prime_list)
        self.assertEqual(is_grid, 'NO')

    def test_give_asdfgh_zxcvbn_lkoiuy_rfgtyu_poiuyt_loveyo_is_not_grid(self):
        prime_list = ['asdfgh', 'zxcvbn', 'lkoiuy', 'rfgtyu', 'poiuyt', 'loveyo']
        is_grid = is_gridChallenge(prime_list)
        self.assertEqual(is_grid, 'NO')

    def test_give_eibjbwsp_ptfxehaq_jxipvfga_rkefiyub_rkefiyub_kalwfhfj_nflvjznh_nflvjznh_is_not_grid(self):
        prime_list = ['eibjbwsp', 'ptfxehaq', 'jxipvfga', 'rkefiyub', 'rkefiyub', 'kalwfhfj', 'nflvjznh', 'nflvjznh']
        is_grid = is_gridChallenge(prime_list)
        self.assertEqual(is_grid, 'NO')

    def test_give_abcde_lllll_qqqqq_ttttt_vvvvv_is_grid(self):
        prime_list = ['abcde', 'lllll', 'qqqqq', 'ttttt', 'vvvvv']
        is_grid = is_gridChallenge(prime_list)
        self.assertEqual(is_grid, 'YES')

    def test_give__is_grid(self):
        prime_list = []
        is_grid = is_gridChallenge(prime_list)
        self.assertEqual(is_grid, 'YES')

    def test_give_ab_kk_is_grid(self):
        prime_list = ['ab', 'kk']
        is_grid = is_gridChallenge(prime_list)
        self.assertEqual(is_grid, 'YES')

    def test_give_iobhposylbmxuxq_bpdbysamgxlzwxl_mszdikmnriqowcr_pzayixomdqfhnpj_oipskkcbasumvls_eawmuhmkhxohkxl_bmjuiqvykhjcgkb_uqhmhwsxfyliwdg_lwtstpmsxhmbapl_tpsevgaeyzpialk_ldrlqvcrzceyxod_acxghpfzfvlukad_kpmtbdqztfvqlzc_ftaffeffmexgksp_tgkbtstopxzrwpx_is_not_grid(self):
        prime_list = ['iobhposylbmxuxq', 'bpdbysamgxlzwxl', 'mszdikmnriqowcr', 'pzayixomdqfhnpj', 'oipskkcbasumvls', 'eawmuhmkhxohkxl', 'bmjuiqvykhjcgkb', 'uqhmhwsxfyliwdg', 'lwtstpmsxhmbapl', 'tpsevgaeyzpialk', 'ldrlqvcrzceyxod', 'acxghpfzfvlukad', 'kpmtbdqztfvqlzc', 'ftaffeffmexgksp', 'tgkbtstopxzrwpx']
        is_grid = is_gridChallenge(prime_list)
        self.assertEqual(is_grid, 'NO')

    def test_give_asdfghjklo_poiuytredf_bvcxzasdfr_loikjuhygt_plokimnbvc_zaswefvbhy_kjiuhgfcxs_lpoikjubvc_mjkioplszq_bvcxfrgthy_is_not_grid(self):
        prime_list = ['asdfghjklo', 'poiuytredf', 'bvcxzasdfr', 'loikjuhygt', 'plokimnbvc', 'zaswefvbhy', 'kjiuhgfcxs', 'lpoikjubvc', 'mjkioplszq', 'bvcxfrgthy']
        is_grid = is_gridChallenge(prime_list)
        self.assertEqual(is_grid, 'NO')

