from selenium.webdriver.common.by import By
from Atid_store.Base_Test.Base_test import *
from Atid_store.Locators.locators import *


class AtidStore_page(BaseTest, Locators):

    # def _init_(self,driver):
    #     super()._init_(driver)

    def open(self):
        self.driver.get(self.atid_url)
        self.driver.maximize_window()

    def execute_test_store(self):
        self._click(By.XPATH, self.store_button)
        self._click(By.XPATH, self.abchor_bracelet)
        self._click(By.XPATH, self.add_to_chart)
        self._click(By.XPATH, self.view_prduct_chart)

        assert self.check_product(self.name_product) == "Anchor Bracelet"
        #self._click(By.XPATH, self.coupon_box)
        self._type(By.XPATH, self.coupon_box, "1234")
        self._click(By.XPATH, self.apply_copuon)
        # assert self.message(self.error_store_xpath) == 'Coupon "1234" does not exist!'

    def execute_men_acceseries(self):
        self._click(By.XPATH, self.MenAccesories_path)
        self._click(By.XPATH, self.Black_Hoodie_path)
        self._click(By.XPATH, self.AddToCart_Black_Hoodie_path)
        self._click(By.XPATH, self.ViewCart_Black_Hoodie_path)

        assert self.check_product(self.Item_nameBlack_Hoodie_path) == "Black Hoodie"
        #self._click(By.XPATH, self.coupon_box_Black_Hoodie_path)
        self._type(By.XPATH, self.coupon_box_Black_Hoodie_path, "12345")
        self._click(By.XPATH, self.AppCoupon_Black_Hoodie_path)
        #assert self.message(self.error_store_xpath) == "Coupon 12345 does not exist!"


    def execute_test_Women_product(self):

        self._click(By.XPATH, self.women_button)
        self._click(By.XPATH, self.click_shoulder_handbag)
        self._click(By.XPATH, self.added_to_chart)
        self._click(By.XPATH, self.view_to_chart)
        assert self.check_product(self.products_names) == "Black Over-the-shoulder Handbag"
        self._type(By.XPATH, self.coupon_boxw, "1234coupon")
        self._click(By.XPATH, self.click_copun)
        # assert self.message(self.error_xpath) == 'Coupon "654651" does not exist!'


    def execute_accsesories_product(self):
        self._click(By.XPATH, self.Accesories_path)
        self._click(By.XPATH, self.BuddhaBracelet_path)
        self._click(By.XPATH, self.BuddhaBracelet_Bracelet_path)
        self._click(By.XPATH, self.BuddhaBuddhaBracelet_path)
        assert self.check_product(self.Item_nameBuddhaBracelet_path) == "Buddha Bracelet"
        self._type(By.XPATH, self.coupon_box_BuddhaBracelet_path, '654651')
        self._click(By.XPATH, self.AppCoupon_BuddhaBracelet_path)
