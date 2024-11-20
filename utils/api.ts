// interface BingImage {
//     url: string;
//     title: string;
//     caption: string;
//   }
  
//   const BASE_URL = 'https://cn.bing.com/HPImageArchive.aspx?format=js';
  
//   export async function getBingWallPapers(idx = 0, n = 10): Promise<BingImage[]> {
//     const API_URL = `https://cn.bing.com/HPImageArchive.aspx?format=js&idx=${idx}&n=${n}`;
//     try {
//       const response = await fetch(API_URL);
//       const json = await response.json();
//       console.log('Fetched Images:', json); // 打印完整的 API 返回值
//       return json.images.map((img: any) => ({
//         url: `https://cn.bing.com${img.url}`, // 拼接完整的图片 URL
//         title: img.title,
//         caption: img.caption,
//       }));
//     } catch (error) {
//       console.error('Error fetching wallpapers:', error);
//       return [];
//     }
//   }
  
interface BingImage {
  url: string;
  title: string;
  caption: string;
}

const BASE_URL = 'https://cn.bing.com/HPImageArchive.aspx?format=js';

export async function getBingWallPapers(idx = 0, n = 10): Promise<BingImage[]> {
  const API_URL = `${BASE_URL}&idx=${idx}&n=${n}`;
  try {
    const response = await fetch(API_URL);
    const json = await response.json();
    console.log('Fetched Images:', json); // 打印完整的 API 返回值
    return json.images.map((img: any) => ({
      url: `https://cn.bing.com${img.url}`, // 拼接完整的图片 URL
      title: img.title,
      caption: img.caption,
    }));
  } catch (error) {
    console.error('Error fetching wallpapers:', error);
    return [];
  }
}

// 添加新的函数
export async function fetchPropertyAddresses() {
  const API_URL = 'https://repair-or-replace-back-end.onrender.com/api/properties/';
  try {
    const response = await fetch(API_URL);
    const data = await response.json();
    console.log('Fetched Property Addresses:', data); // 打印返回数据
    return data.map((property: any) => ({
      id: property.id,
      address_line_1: property.address_line_1,
      appliances: property.appliances.map((appliance: any) => ({
        id: appliance.id,
        name: appliance.name,
        brand: appliance.brand,
        model: appliance.model,
        current_status: appliance.current_status,
      })),
    }));
  } catch (error) {
    console.error('Error fetching property addresses:', error);
    return [];
  }
}
