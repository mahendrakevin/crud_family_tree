-- 3. Buat query untuk mendapatkan semua anak Budi
SELECT nama FROM `families` WHERE families.child_of=(SELECT MIN(parent_id) FROM families)

-- 4. Buat query untuk mendapatkan cucu dari budi
SELECT nama FROM `families` WHERE families.child_of!=(SELECT MIN(parent_id) FROM families)

-- 5. Buat query untuk mendapatkan cucu perempuan dari budi
SELECT nama FROM `families` WHERE families.child_of != (SELECT MIN(parent_id) FROM families) AND families.jenis_kelamin='Wanita'

-- 6. Buat query untuk mendapatkan bibi dari Farah
SELECT nama FROM `families` WHERE families.child_of = (SELECT MIN(parent_id) FROM families) AND families.jenis_kelamin='Wanita'

-- 7. Buat query untuk mendapatkan sepupu laki-laki dari Hani
SELECT nama FROM `families` WHERE families.child_of != (SELECT MIN(parent_id) FROM families) AND families.jenis_kelamin='Pria'